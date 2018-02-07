# coding=utf-8
from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    """Returns Index route"""
    user = {'username': 'Ebenezer'}
    return render_template('index.html', title='Microblog', user=user)
