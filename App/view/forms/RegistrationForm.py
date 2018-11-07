from flask_wtf import FlaskForm
from flask_babel import lazy_gettext as _1
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired , ValidationError, Email, EqualTo
from App.models import User

class RegistrationForm(FlaskForm):
    username = StringField(_1('Username'), validators=[DataRequired()])
    email = StringField(_1('Email'), validators=[DataRequired(), Email()])
    password = PasswordField(_1('Password'), validators=[DataRequired()])
    password2 = PasswordField(
        _1('Repeat Password'), validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_1('Register'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_1('Please use a different username.'))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_1('Please use a different email address.'))
    def validate_image(form, field):
        if field.data:
            field.data = re.sub(r'[^a-z0-9_.-]', '_', field.data)