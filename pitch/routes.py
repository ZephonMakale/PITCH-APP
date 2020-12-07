from flask import render_template, url_for, flash, redirect
from pitch import app, db, bcrypt
from pitch.forms import RegistrationForm, LoginForm
from pitch.models import User, Post
from flask_login import login_user

posts = [
    {
        'author': 'Zephon Makale',
        'title': 'Pitch 1',
        'content': 'I am an experienced Graphics Designer with 3 years of active work',
        'date_posted': 'December 6th, 2020'
    },
    {
        'author': 'B. Kamau',
        'title': 'Pitch 2',
        'content': 'I am an experienced Web Designer with 2 years of active work',
        'date-posted': 'December 7th, 2020'
    },

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in','success')
        return redirect(url_for('login'))
    return render_template('register.html', title = 'Register', form = form)

@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful, please check your email and password again', 'danger')
    return render_template('login.html', title = 'Login', form = form)
