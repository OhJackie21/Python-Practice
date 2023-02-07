from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def register(cls,data):
        query = """
                INSERT INTO users(first_name, last_name, email, password, created_at, updated_at)
                VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());
                """
        results = connectToMySQL('sasquatch').query_db(query,data)
        return results
    
    @staticmethod
    def user_validate(user_info):
        is_valid = True
        if len(user_info['first_name']) <= 0 or len(user_info['first_name']) <= 0 or len(user_info['last_name']) <= 0:
            flash("Form must be filled")
        if len(user_info['first_name']) < 2: 
            flash("First name must be at least 2 characters")
            is_valid = False
        if len(user_info['last_name']) < 2: 
            flash("Last name must be at least 2 characters")
            is_valid = False
        if len(user_info['email']) > 0 and not EMAIL_REGEX.match(user_info['email']):
            flash("**Invalid email address!**")
            is_valid = False
        if len(user_info['password']) < 8: 
            flash("Password must be at least 8 characters")
        if user_info['password'] != user_info['confirm']:
            flash("Password does not match")
            is_valid = False
        
        return is_valid

    
    @classmethod
    def user_info(cls,data):
        query = """
                    SELECT * FROM users
                    WHERE id = %(id)s
                """
        results = connectToMySQL('sasquatch').query_db(query, data)
        return cls(results[0])

    @classmethod
    def email(cls,data):
        query = """
                SELECT * FROM users
                WHERE email = %(email)s;
                """
        results = connectToMySQL('sasquatch').query_db(query, data)
        if len(results) < 1: #if we don't find a match in the db
            return False
        return cls(results[0])
