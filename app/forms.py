from flask_wtf import  FlaskForm
from wtforms import StringField, SubmitField, PasswordField,BooleanField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, EqualTo

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password2')])
    password2 = PasswordField('Password once again', validators=[DataRequired(), EqualTo('password')])
    about = TextAreaField('About me', default='')
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username=StringField('Username', validators=[DataRequired()])
    password=PasswordField('Password', validators=[DataRequired()])
    submit= SubmitField('Login')