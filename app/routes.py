#app/routes.py

from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'TOLES'}
    posts = [
        {
            'author': {'username': 'Margit'},
            'body': 'FOUL TARNISHED. IN SEARCH OF THE ELDEN RING. ENBOLDED BY THE FLAME OF AMBITION'
        },
        {
            'author': {'username': 'Maliketh'},
            'body': 'Oh Death... Become my blade once more...'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)