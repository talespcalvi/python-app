#app/routes.py

from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login solicitado para o user={}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)