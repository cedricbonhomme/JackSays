from flask import flash
from flask.ext.wtf import Form
from flask.ext.babel import lazy_gettext
from wtforms import TextField, TextAreaField, PasswordField, BooleanField, SubmitField, validators
from flask.ext.wtf.html5 import EmailField
from flask_wtf import RecaptchaField    

from web.models import User



class SigninForm(Form):
    """
    Sign in form.
    """
    login = TextField("Login", [validators.Length(min=6, max=35), validators.Required("Please enter your login.")])
    submit = SubmitField("Log In")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        #user = User.query.filter(User.email == self.email.data).first()
        return True
        """
        if user and user.check_password(self.password.data) and user.activation_key == "":
            return True
        elif user and user.activation_key != "":
            flash('Account not confirmed', 'danger')
            return False
        else:
            flash('Invalid email or password', 'danger')
            #self.email.errors.append("Invalid email or password")
            return False"""