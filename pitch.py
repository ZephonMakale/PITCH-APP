from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'a9e5c966dbd643ddca1c4249c0036039'

posts = [
    {
        'author': 'Zephon Makale',
        'title': 'Pitch 1',
        'content': 'I am an experienced Graphics Designer with 3 years of active work',
        'date': 'December 6th, 2020'
    },
    {
        'author': 'B. Kamau',
        'title': 'Pitch 2',
        'content': 'I am an experienced Web Designer with 2 years of active work',
        'date': 'December 7th, 2020'
    },

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title = 'Register', form = form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form = form)


if __name__ == ('__main__'):
        app.run(debug=True)
