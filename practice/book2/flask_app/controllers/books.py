from flask import Flask, render_template, redirect, request
from flask_app import app
from flask_app.models.sighting import Sighting
from flask_app.models.user import User


@app.route('/books')
def books():
    books = Book.all_boooks()
    return render_template('books.html', books = books)

@app.route('/bkfave/<int:id>')
def bkfave(id):
    data = { "id": id }
    favebooks = Book.bookfaves(data)
    notfavea = User.notfavea(data)
    return render_template('bookfavorite.html', favebooks = favebooks, notfavea = notfavea)


@app.route('/faveauthor', methods = ['POST'])
def faveauthor():
    data ={
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    User.faveauthor(data)
    return redirect(f"/bkfave/{request.form['book_id']}")

@app.route('/addbook', methods=['POST'])
def addbook():
    Book.addbook(request.form)
    return redirect('/books')