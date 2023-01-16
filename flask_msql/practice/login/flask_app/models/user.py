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
    def add(cls,data):
        query = """
                INSERT INTO user(first_name, last_name, email, password, created_at, updated_at)
                VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());
            
                """
        results = connectToMySQL('login_registration_schema').query_db(query, data)
        return results

    @staticmethod
    def validate_add(user_info):
        is_valid = True
        if len(user_info['first_name']) <= 0 or len(user_info['last_name']) <= 0 or len(user_info['email']) <= 0 or len(user_info['password']) <= 0 or len(user_info['confirm']) <=0:
            flash("All fields must be filled", "all_fields")
            is_valid = False
        if len(user_info['first_name']) < 2:
            flash("First Name must be at least 2 characters long", "first_name")
            is_valid = False
        if len(user_info['last_name']) < 2:
            flash("Last Name must be at least 2 characters long", "last_name")
            is_valid = False
        if len(user_info['email']) > 0 and not EMAIL_REGEX.match(user_info['email']):
            flash("**Invalid email address!**", "email")
            is_valid = False
        if len(user_info['password']) < 8:
            flash("Password must least be 8 characters long")
            is_valid = False
        if user_info['password'] != user_info['confirm']:
            flash("Password does not match", "notmatch")
            is_valid = False

        return is_valid

    @classmethod
    def user_info(cls,data):
        query = """
            SELECT * FROM user
            WHERE id = %(id)s
        """
        results = connectToMySQL('login_registration_schema').query_db(query, data)
        return cls(results[0])