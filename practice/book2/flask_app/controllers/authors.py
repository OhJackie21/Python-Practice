from flask import Flask, render_template, redirect, request
from flask_app import app
from flask_app.models.user import User
from flask_app.models.sighting import Sighting

@app.route('/')
def index():
    return redirect('/alist')

@app.route('/alist')
def alist():
    authors = User.all_author()
    return render_template('index.html', authors = authors)

@app.route('/afave/<int:id>')
def afave(id):
    data = { 'id': id }
    authors = User.authorfave(data)
    notbooks = Sighting.notfaveb(data)
    return render_template('afavorite.html', authors = authors, notbooks = notbooks)

@app.route('/addauthor', methods=['POST'])
def addauthor():
    User.add_author(request.form)
    return redirect('/')

@app.route('/favebook', methods = ['POST'])
def favebook():
    data ={
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Sighting.favebook(data)
    return redirect(f"/afave/{request.form['author_id']}")