from flask import Flask, render_template, redirect, request

from flask_app import app
from flask_app.models.dojo import Dojo


@app.route('/')
def index():
    return redirect('/home')

@app.route('/home')
def home():
    dojos = Dojo.get_all()
    return render_template('index.html', dojos = dojos)

@app.route('/dojos/<int:id>')
def dojo_names(id):
    data = { "id": id }
    dojos = Dojo.ninjas_in_dojo(data)
    return render_template('ninjas.html', dojos = dojos)

@app.route('/add_dojo', methods=['POST'])
def add_dojo():
    Dojo.add(request.form)
    return redirect('/home')