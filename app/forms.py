from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired



class TitleForm(FlaskForm):
    title = StringField('Title: ', validators=[DataRequired()])
    submit = SubmitField('Submit')

class PostForm(FlaskForm):
    tweet = StringField('What are you doing?', validators=[DataRequired()])
    submit = SubmitField('Tweet')
