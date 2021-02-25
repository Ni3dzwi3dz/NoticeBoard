from app import app
from flask import render_template
from app.forms import RegisterForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    form = RegisterForm()
    return render_template('register.html', form=form)
