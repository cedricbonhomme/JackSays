#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Jack Says - A Web-Based, "Simon Says"-like, multiplayer game.
# Copyright (C) 2015  https://github.com/cedricbonhomme/JackSays
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from flask import flash
from flask.ext.wtf import Form
from wtforms import TextField, SubmitField, validators

from web.models import User
from web import USERS


class SigninForm(Form):
    """
    Sign in form.
    """
    login = TextField("Login", [validators.Length(min=2, max=35), validators.Required("Please enter your nickname.")])
    avatar = TextField("Avatar")
    submit = SubmitField("Log In")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        if self.login.data in USERS:
            flash('Nickname already taken', 'danger')
            return False

        return True