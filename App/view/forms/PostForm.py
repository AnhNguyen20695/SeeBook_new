from flask_wtf import FlaskForm
from flask_babel import lazy_gettext as _1
from wtforms import TextAreaField , SubmitField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    post = TextAreaField(_1('Post something'), validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField(_1('Post'))