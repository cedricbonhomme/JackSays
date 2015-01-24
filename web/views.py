#! /usr/bin/env python
# -*- coding: utf-8 -*-

from gevent import monkey
monkey.patch_all()

import time
from threading import Thread
from flask import render_template, redirect, url_for, session, request, g, flash
from flask.ext.socketio import SocketIO, emit, join_room, leave_room, \
    close_room, disconnect

from web import app, socketio, USERS
from form import SigninForm
from models import User

thread = None
from flask.ext.login import LoginManager, login_user, logout_user, \
                            login_required, current_user, AnonymousUserMixin
from flask.ext.principal import Principal, Identity, AnonymousIdentity, \
                                identity_changed, identity_loaded, Permission,\
                                RoleNeed, UserNeed

login_manager = LoginManager()
login_manager.init_app(app)

from games.utils import WaitGame
from core import load_game


#
# Custom error pages.
#
@app.errorhandler(401)
def authentication_required(e):
    flash('Authentication required.', 'info')
    return redirect(url_for('login'))

@app.errorhandler(403)
def authentication_failed(e):
    flash('Forbidden.', 'danger')
    return redirect(url_for('login'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500


def redirect_url(default='login'):
    return request.args.get('next') or \
            request.referrer or \
            url_for(default)


#
# Management of the user's session.
#
@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    # Set the identity user object
    identity.user = current_user

@app.before_request
def before_request():
    g.user = current_user
    if g.user.is_authenticated():
        pass

@login_manager.user_loader
def load_user(nic):
    # Return an instance of the User model
    #return User.query.filter(User.email == email).first()
    for user in USERS:
        if user == nic:
            return USERS[user]
    return None


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Log in view.
    """
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('login'))

    g.user = AnonymousUserMixin()
    form = SigninForm()
    print form.login.data

    if form.validate_on_submit():
        user = User(form.login.data, 0)
        USERS[user.nic] = user
        login_user(user)
        g.user = user
        session['login'] = form.login.data
        flash("Logged in successfully.", 'success')
        return redirect(url_for('index'))
    return render_template('customize.html', form=form)

@app.route('/customize')
def customize():
    form = SigninForm()
    return render_template('customize.html',form=form)

@app.route('/')
def index():
    form = SigninForm()
    return render_template('index.html', user=g.user, form=form)
@app.route('/play')
def play():
    w = WaitGame()
    duration = 60.0
    load_game(w)
    return render_template('play.html')
