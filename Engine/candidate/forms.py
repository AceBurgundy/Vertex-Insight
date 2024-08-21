from wtforms.validators import DataRequired, Email
from wtforms import StringField, TextAreaField
from flask_wtf import FlaskForm

class CommentForm(FlaskForm):
    """
    A comment template using flaskform.
    """
    email: StringField = StringField('Email', validators=[DataRequired(), Email()])
    username: StringField = StringField('Username')
    text: TextAreaField = TextAreaField('Comment', validators=[DataRequired()])
