from flask import render_template
from app import app
from app.forms import LoginForm


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'swapneel'}
    posts = [
        {
            'author':{'username': 'Swapneel'},
            'body': 'Hello World'
        },
        {
            'author':{'username': 'Ira'},
            'body': 'Python is cool'
        }
    ]
        
    return render_template('index.html', title='Web Page', user=user,posts=posts)
