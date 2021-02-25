from flask_wtf import  FlaskForm
from wtforms import StringField, SubmitField, PasswordField,BooleanField, TextAreaField
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Password once again', validators=[DataRequired()])
    about = TextAreaField('About me', default='')
    submit = SubmitField('Register')

