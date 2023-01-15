from flask import Flask, render_template, redirect, request
from flask_app import app
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route('/')
def index():
    return redirect('/alist')

@app.route('/alist')
def alist():
    authors = Author.all_author()
    return render_template('index.html', authors = authors)

@app.route('/afave/<int:id>')
def afave(id):
    data = { 'id': id }
    authors = Author.authorfave(data)
    notbooks = Book.notfaveb(data)
    return render_template('afavorite.html', authors = authors, notbooks = notbooks)

@app.route('/addauthor', methods=['POST'])
def addauthor():
    Author.add_author(request.form)
    return redirect('/')

@app.route('/favebook', methods = ['POST'])
def favebook():
    data ={
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Book.favebook(data)
    return redirect(f"/afave/{request.form['author_id']}")