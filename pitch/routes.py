from flask import render_template, url_for, flash, redirect
from pitch import app
from pitch.forms import RegistrationForm, LoginForm
from pitch.models import User, Post

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
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)

@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@pitch.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful, please check your username and password again', 'danger')
    return render_template('login.html', title = 'Login', form = form)
