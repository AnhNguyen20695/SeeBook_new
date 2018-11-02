from flask_wtf import FlaskForm
from flask_babel import lazy_gettext as _1
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User

class LoginForm(FlaskForm):
    username = StringField(_1('Username'), validators=[DataRequired()])
    password = PasswordField(_1('Password'), validators=[DataRequired()])
    remember_me = BooleanField(_1('Remember Me'))
    submit = SubmitField(_1('Sign In'))


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

class EditProfileForm(FlaskForm):
    username = StringField(_1('Username'), validators=[DataRequired()])
    about_me = TextAreaField(_1('About me'), validators=[Length(min=0, max=140)])
    submit = SubmitField(_1('Submit'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(_1('Please use a different username.'))

    def validate_image(form, field):
        if field.data:
            field.data = re.sub(r'[^a-z0-9_.-]', '_', field.data)

class PostForm(FlaskForm):
    post = TextAreaField(_1('Post something'), validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField(_1('Post'))