from flask_wtf import FlaskForm
from wtforms import TextField, validators


class CommentForm(FlaskForm):
    text = TextField('Comment', [validators.Required()])
