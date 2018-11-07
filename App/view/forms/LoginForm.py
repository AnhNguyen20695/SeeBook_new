from flask_wtf import FlaskForm
from flask_babel import lazy_gettext as _1
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField(_1('Username'), validators=[DataRequired()])
    password = PasswordField(_1('Password'), validators=[DataRequired()])
    remember_me = BooleanField(_1('Remember Me'))
    submit = SubmitField(_1('Sign In'))