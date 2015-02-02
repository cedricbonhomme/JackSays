#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for, session, request, \
                    g, flash
from flask.ext.login import LoginManager, login_user, login_required, \
                            current_user

from web import app, USERS
from form import SigninForm
from models import User

login_manager = LoginManager()
login_manager.init_app(app)

#
# Custom error pages.
#
@app.errorhandler(401)
def authentication_required(e):
    flash('Authentication required.', 'info')
    return redirect(url_for('index'))

@app.errorhandler(403)
def authentication_failed(e):
    flash('Forbidden.', 'danger')
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500


def redirect_url(default='index'):
    return request.args.get('next') or \
            request.referrer or \
            url_for(default)

#
# Management of the user's session.
#
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

#
# Pages
#
@app.route('/')
def index():
    """
    Main page.
    """
    form = SigninForm()
    return render_template('index.html', user=g.user, form=form)

@app.route('/gender')
def gender():
    return render_template('gender.html')

@app.route('/customize', methods=['GET', 'POST'])
def customize():
    """
    This page enables the user to customize its avatar.
    """
    form = SigninForm()

    if form.validate_on_submit():
        user = User(form.login.data, avatar=form.avatar.data, score=0)
        USERS[user.nic] = user
        login_user(user)
        g.user = user
        session['login'] = form.login.data
        flash("Logged in successfully.", 'success')
        return redirect(url_for('play'))

    return render_template('customize.html', form=form)

@app.route('/play')
@login_required
def play():
    """
    Games are loaded in this page wich maintains
    a WebSocket between the client and the server.
    """
    return render_template('play.html')

@app.route('/credit')
def credit():
    """
    Credit page/
    """
    return render_template('credit.html')
