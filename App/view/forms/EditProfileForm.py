from flask_wtf import FlaskForm
from flask_babel import lazy_gettext as _1
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from App.models import User

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