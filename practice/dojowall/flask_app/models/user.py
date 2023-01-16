from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User: 
    def __init__(self, data):
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
        results = connectToMySQL('dojowall').query_db(query,data)
        return results
    
    @staticmethod
    def validated_add(user):
        is_valid = True
        
        #this here verifies if the email is taken by checking the database
        query = """
                SELECT * FROM users
                WHERE email = %(email)s
                """
        results = connectToMySQL('dojowall').query_db(query,user)
        if len(results) >=1:
            flash("Email already taken", "email")
            is_valid = False


        if len(user['first_name']) < 2:
            flash('First Name must be at least 2 characters', 'first_name')
            is_valid = False
        if len(user['last_name']) < 2:
            flash('Last Name must be at least 2 characters', 'last_name')
            is_valid = False
        if len(user['email']) <= 0:
            flash('Email is required', 'email')
            is_valid = False
        if len(user['email']) > 0 and not EMAIL_REGEX.match(user['email']):
            flash("**Invalid email address!**", 'email')
            is_valid = False
        if len(user['password']) <= 0:
            flash('Password is required', "password")
            is_valid = False
        if len(user['password']) < 5:
            flash('Password must be at least 5 characters long', 'password')
            is_valid = False
        if len(user['confirm']) <= 0:
            flash('Confirm password is required', 'password2')
            is_valid = False
        if len(user['confirm']) < 5:
            flash('Password must be at least 5 characters long', 'password2')
            is_valid = False
        if user['password'] != user['confirm']:
            flash("Password does not match")
            is_valid = False
        
        return is_valid

    @classmethod
    def getid(cls, data):
        query = """
                    SELECT * FROM users
                    WHERE id = %(id)s
                """
        results = connectToMySQL('dojowall').query_db(query, data)
        return cls(results[0])
        

    @classmethod
    def getemail(cls, data):
        query = """
                SELECT * FROM users
                WHERE email = %(email)s
                """
        results = connectToMySQL('dojowall').query_db(query, data)
        if len(results) < 1: #if we don't find a match in the db
            return False
        return cls(results[0])     
