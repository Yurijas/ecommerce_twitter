from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo



class TitleForm(FlaskForm):
    title = StringField('Title: ', validators=[DataRequired()])
    submit = SubmitField('Submit')

class PostForm(FlaskForm):
    tweet = StringField('What are you doing?', validators=[DataRequired()])
    submit = SubmitField('Tweet')

class LoginForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    first_name = StringField('First Name:', validators=[DataRequired()])
    last_name = StringField('Last Name:', validators=[DataRequired()])
    username = StringField('Username:', validators=[DataRequired()])
    email = StringField('E-mail:', validators=[DataRequired(), Email()])
    age = IntegerField('Age:')
    bio = StringField('Bio:')
    url = StringField('Profile Pic URL:')
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Re-type Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    # setup validation methods to be checked when form is submitted
    # TODO: create validation methods
