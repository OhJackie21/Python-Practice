from flask import render_template, redirect, request
from app import app

@app.route('/') # root / home
def home():
    return render_template('index.html') 

@app.route('/say-hello')
def say_hello():
    return 'Hello'

