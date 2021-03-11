from app import app, db
from flask import render_template, flash, redirect, request, url_for
from app.forms import RegisterForm, LoginForm, UserEditForm, AddNoticeForm
from app.models import User
from flask_login import current_user, login_user, login_required
from werkzeug.urls import url_parse
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

#Users - register, login etc

@app.before_request
def track_time():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.now()
        db.session.commit()

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()

    #after submitting register form
    if form.validate_on_submit():
        user=User(
            username=form.username.data,
            email= form.email.data,    
            city= form.city.data,
            about= form.about.data or ''
            )
        user.set_pass(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash(f'User {form.username.data} registered successfully')

        return redirect(url_for('login'))

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()

    #user already logged in
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    #after submiting login
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_pass(form.password.data):
            flash('Either username or password is incorrect')
            return redirect(url_for('login'))
        else:
            login_user(user)
        
        next = request.args.get('next')
        if not next or url_parse(next).netloc == '':
            return redirect(url_for('index'))
        
        return redirect(next)

    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    pass

@app.route('/user/edit')
def edit_profile():
    form=UserEditForm(current_user.username)

    return render_template('user-edit.html', form=form)

@app.route('/user/<username>')
@login_required
def user_profile(username):
    user=User.query.filter_by(username=username).first_or_404()

    return render_template('user.html', user=user)

#Notices - adding, reading etc.

@app.route('/notice/add')
@login_required
def add_notice():
    form= AddNoticeForm()

    return render_template('add-notice.html', form=form)



#Error handling
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html')