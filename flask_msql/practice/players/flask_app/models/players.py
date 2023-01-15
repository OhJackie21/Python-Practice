from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



class Players:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.user_name = data['user_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM players;"
        results = connectToMySQL('players').query_db(query)
        players = []
        for i in results:
            players.append( cls(i) )
        return players
    
    @classmethod
    def save(cls, data): 
        query = "INSERT INTO players(first_name, last_name, user_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(user_name)s, %(email)s, NOW(), NOW() );"
        result = connectToMySQL('players').query_db(query, data)
        return result
    
    @classmethod
    def update(cls,data):
        query = "UPDATE players SET first_name = %(first_name)s, last_name = %(last_name)s, user_name = %(user_name)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
        result = connectToMySQL('players').query_db(query, data)
        return result
    
    @classmethod
    def player_info(cls,data):
        query = "SELECT * FROM players WHERE id = %(id)s;"
        result = connectToMySQL('players').query_db(query, data)
        return cls(result[0])

    @classmethod
    def remove(cls, data):
        query = "DELETE FROM players WHERE id = %(id)s;"
        result = connectToMySQL('players').query_db(query, data)
        return result

    @staticmethod
    def validate_add(players):
        is_valid = True 
        if len(players['first_name']) <= 0:
            flash("**First Name is required.**", 'first_name')
            is_valid = False
        if len(players['last_name']) <= 0:
            flash("**Last Name is required.**", 'last_name')
            is_valid = False
        if len(players['user_name']) <= 0:
            flash("**User Name is required.**", "user_name")
            is_valid = False
        if len(players['email']) <= 0:
            flash("**Email is required.**", "email")
        if len(players['email']) > 0 and not EMAIL_REGEX.match(players['email']):
            flash("**Invalid email address!**", "email_invalid")
            is_valid = False
        return is_valid
        