from flask import flash
from flask.ext.wtf import Form
from flask.ext.babel import lazy_gettext
from wtforms import TextField, TextAreaField, PasswordField, BooleanField, SubmitField, validators
from flask.ext.wtf.html5 import EmailField
from flask_wtf import RecaptchaField

from web.models import User
from web import USERS


class SigninForm(Form):
    """
    Sign in form.
    """
    login = TextField("Login", [validators.Length(min=2, max=35), validators.Required("Please enter your login.")])
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