#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import flash
from flask.ext.wtf import Form
from wtforms import TextField, SubmitField, validators

from web.models import User
from web import USERS


class SigninForm(Form):
    """
    Sign in form.
    """
    login = TextField("Login", [validators.Length(min=2, max=35), validators.Required("Please enter your login.")])
    avatar = TextField("Avatar")
    submit = SubmitField("Log In")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        if self.login.data in USERS:
            flash('Login already taken', 'danger')
            return False

        return True