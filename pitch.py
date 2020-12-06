from flask import Flask, render_template


app = Flask(__name__)

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

if __name__ == ('__main__'):
        app.run(debug=True)
