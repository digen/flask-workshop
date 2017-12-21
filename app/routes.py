from flask import render_template
from app import app

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
