from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author


class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.faveauthor = []
        
    
    @classmethod
    def all_boooks(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL('books_schema2').query_db(query)
        books = []
        for i in results:
            books.append( cls(i) )
        return books

    @classmethod
    def bookfaves(cls,data):
        query = "SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id LEFT JOIN authors ON authors.id = favorites.author_id WHERE books.id = %(id)s;"
        results = connectToMySQL('books_schema2').query_db(query,data)
        books = cls( results[0])
        for bk in results:
            if bk['authors.id'] == None:
                break
            data = {
                "id": bk['authors.id'],
                "name": bk['name'],
                "created_at": bk['created_at'],
                "updated_at": bk['updated_at']
            }
            books.faveauthor.append(author.Author(data))
        return books
    
    @classmethod
    def notfaveb(cls, data):
        query = "SELECT * FROM books WHERE books.id NOT IN (SELECT book_id FROM favorites WHERE author_id = %(id)s);"
        results = connectToMySQL('books_schema2').query_db(query,data)
        books = []
        for i in results:
            books.append( cls(i) )
        return books
    
    @classmethod
    def favebook(cls,data):
        query = "INSERT INTO favorites(author_id, book_id) VALUES(%(author_id)s, %(book_id)s);"
        results = connectToMySQL('books_schema2').query_db(query,data)
        return results

    @classmethod
    def addbook(cls,data):
        query = "INSERT INTO books(title, num_of_pages, created_at, updated_at) VALUES(%(title)s, %(num_of_pages)s, NOW(), NOW());"
        results = connectToMySQL('books_schema2').query_db(query,data)
        return results