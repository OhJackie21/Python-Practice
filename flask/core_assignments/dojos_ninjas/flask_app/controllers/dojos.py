from flask import Flask, render_template, redirect, request

from flask_app.models.dojo import Dojo
from flask_app import app

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/home')

@app.route('/home')
def home():
    dojos = Dojo.get_all()
    return render_template('index.html', )

@app.route('/add_ninja')
def addform():
    return render_template('addninja.html')