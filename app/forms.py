from flask_wtf import  FlaskForm
from wtforms import StringField, SubmitField, PasswordField,BooleanField, \
    TextAreaField, FileField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, EqualTo
from flask_login import current_user
from app.models import User


#USERS

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), 
            EqualTo('password2')])
    password2 = PasswordField('Password once again', validators=[DataRequired(),
            EqualTo('password')])
    about = TextAreaField('About me', default='')
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username=StringField('Username', validators=[DataRequired()])
    password=PasswordField('Password', validators=[DataRequired()])
    submit= SubmitField('Login')

class UserEditForm(FlaskForm):
    user= current_user or User()

    username = StringField('Username', validators=[DataRequired()], 
            default=user.username )
    city = StringField('City', validators=[DataRequired()], 
            default=user.city)
    email = EmailField('Email', validators=[DataRequired()], 
            default= user.email)
    about = TextAreaField('About me', default=user.about)
    submit = SubmitField('Update')

    def __init__(self,original_username, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.original_username=original_username
    
    def validate_username(self, username):
        if username.data != original_username:
            user = User.query.filter_by(username=self.username.data).first()

            if user is not None:
                raise ValidationError('Username already in use')


#Notices

class AddNoticeForm(FlaskForm):
    title=StringField('Title', validators=[DataRequired()])
    body=TextAreaField('Text', validators=[DataRequired()])
    image=FileField('Add cover photo')
    submit=SubmitField('Add')

    
   
