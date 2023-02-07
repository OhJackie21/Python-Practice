from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.controllers.users import User

class Show:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.network = data['network']
        self.release_date = data['release_date']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user = None
    
    @classmethod
    def all_shows(cls):
        query = """
                SELECT * FROM shows
                LEFT JOIN users on shows.user_id = users.id;
                """
        results = connectToMySQL('tvshows').query_db(query)
        shows = []
        if not results: 
            return shows
        for info in results:
            show = cls(results[0])
            row = {
                'id': info['users.id'],
                'first_name': info['first_name'],
                'last_name': info['last_name'],
                'email': info['email'],
                'password': "",
                'created_at': info['users.created_at'],
                'updated_at': info['users.updated_at']

            }
            show.user= User(row)
            shows.append(show)
        return results

    @staticmethod
    def validate_show(show_info):
        is_valid = True
    
        if len(show_info['title']) < 3:
            flash("Title is needed/Not valid information")
            is_valid = False
        if len(show_info['network']) < 3:
            flash("Network is needed/Not valid information")
            is_valid = False
        if show_info['release_date'] == ''  :
            flash("Please input a date")
            is_valid = False
        if len(show_info['description']) < 3:
            flash("Please put a valid Show Description")
            is_valid = False
        
        return is_valid
    

    @classmethod
    def add_show(cls,data):
        query = """
                INSERT INTO shows(title, network, release_date, description, created_at, updated_at, user_id)
                VALUES(%(title)s, %(network)s, %(release_date)s, %(description)s,NOW(), NOW(), %(user_id)s); 
                """
        results = connectToMySQL('tvshows').query_db(query,data)
        return results
    
    @classmethod
    def update_show(cls,data):
        query = """
                UPDATE shows
                SET title = %(title)s, network = %(network)s, release_date = %(release_date)s, description = %(description)s, updated_at = NOW()
                WHERE id = %(id)s
                """
        results = connectToMySQL('tvshows').query_db(query,data)
        return results
    
    @classmethod
    def getidby(cls,data):
        query = """
                SELECT * FROM shows
                WHERE id = %(id)s;
                """
        results = connectToMySQL('tvshows').query_db(query,data)
        return cls(results[0])

    
    @classmethod
    def remove_show(cls, data):
        query = """
                DELETE FROM shows
                WHERE id = %(id)s
                """
        results = connectToMySQL('tvshows').query_db(query,data)
        return results