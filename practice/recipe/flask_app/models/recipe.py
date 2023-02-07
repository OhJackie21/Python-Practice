from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from .user import User

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.date_made = data['date_made']
        self.under_30 = data['under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.users = []


    @classmethod
    def all_recipes(cls):
        query = """
                SELECT * FROM recipes
                JOIN users on recipes.user_id = users.id;
                """
        results = connectToMySQL('recipe').query_db(query)
        print(results)
        recipe = cls(results[0])
        for info in results:
            row = {
                'id': info['users.id'],
                'first_name': info['first_name'],
                'last_name': info['last_name'],
                'email': info['email'],
                'password': "",
                'created_at': info['created_at'],
                'updated_at': info['updated_at']

            }
            recipe.users.append(User(row))
        return results
    

    @classmethod
    def add_recipe(cls,data):
        query = """
                INSERT INTO recipes(name, description, instruction, date_made, under_30, created_at, updated_at, user_id)
                VALUES(%(name)s, %(description)s, %(instruction)s, %(date_made)s, %(under_30)s, NOW(), NOW(), %(user_id)s); 
                """
        results = connectToMySQL('recipe').query_db(query,data)
        return results

    @staticmethod
    def validate_recipe(recipe_info):
        is_valid = True
        
        if len(recipe_info['name']) < 3:
            flash("Name must be at least 3 characters long")
            is_valid = False
        if len(recipe_info['description']) < 3:
            flash("Descriptions must be at least 3 characters long")
            is_valid = False
        if len(recipe_info['instruction']) < 3:
            flash("Instructions must be at least 3 characters long")
            is_valid = False
        if 'under_30' not in recipe_info:
            flash("Yes or No must be selected")
            is_valid = False
        if recipe_info['date_made'] == ''  :
            flash("Please input a date")
            is_valid = False
        
        return is_valid

    @classmethod
    def getidby(cls,data):
        query = """
                SELECT * FROM recipes
                WHERE id = %(id)s;
                """
        results = connectToMySQL('recipe').query_db(query,data)
        return cls(results[0])

    @classmethod
    def update_recipe(cls,data):
        query = """
                UPDATE recipes
                SET name = %(name)s, description = %(description)s, instruction = %(instruction)s, date_made = %(date_made)s, under_30 = %(under_30)s, updated_at = NOW()
                WHERE id = %(id)s
                """
        results = connectToMySQL('recipe').query_db(query,data)
        return results
    
    @classmethod
    def remove_recipe(cls, data):
        query = """
                DELETE FROM recipes
                WHERE id = %(id)s
                """
        results = connectToMySQL('recipe').query_db(query,data)
        return results