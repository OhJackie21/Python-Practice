from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favebooks = []

    @classmethod
    def all_author(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL('books_schema2').query_db(query)
        authors = []
        for i in results:
            authors.append( cls(i) )
        return authors
    
    @classmethod
    def authorfave(cls,data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id LEFT JOIN books on books.id = favorites.book_id WHERE authors.id = %(id)s;"
        results = connectToMySQL('books_schema2').query_db(query,data)
        authors = cls( results[0])
        for info in results:
            if info['books.id'] == None:
                break
            data = {
                "id": info['id'],
                "title": info['title'],
                "num_of_pages": info['num_of_pages'],
                "created_at": info['created_at'],
                "updated_at": info['updated_at']
            }
            authors.favebooks.append(book.Book(data))
        return authors

    @classmethod
    def add_author(cls, data):
        query = "INSERT INTO authors(name, created_at, updated_at) VALUES(%(name)s, NOW(), NOW());"
        results = connectToMySQL('books_schema2').query_db(query,data)
        return results
    
    @classmethod
    def notfavea(cls, data):
        query = "SELECT * FROM authors WHERE authors.id NOT IN (SELECT author_id FROM favorites WHERE book_id = %(id)s);"
        results = connectToMySQL('books_schema2').query_db(query,data)
        authors = []
        for i in results:
            authors.append( cls(i) )
        return authors

    @classmethod
    def faveauthor(cls,data):
        query = "INSERT INTO favorites(author_id, book_id) VALUES(%(author_id)s, %(book_id)s);"
        results = connectToMySQL('books_schema2').query_db(query,data)
        return results
   
