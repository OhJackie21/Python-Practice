from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.controllers.users import User

class Sighting:
    def __init__(self, data):
        self.id = data['id']
        self.location = data['location']
        self.scenario = data['scenario']
        self.date_of_sighting = data['date_of_sighting']
        self.qty_of_sq = data['qty_of_sq']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user = None


    @classmethod
    def all_sightings(cls):
        query = """
                SELECT * FROM sightings
                JOIN users on sightings.user_id = users.id;
                """
        results = connectToMySQL('sasquatch').query_db(query)
        sightings = []
        # will show the next page even though there's nothing in the database
        if not results: 
            return sightings
        for info in results:
            sighting = cls(results[0])
            row = {
                'id': info['users.id'],
                'first_name': info['first_name'],
                'last_name': info['last_name'],
                'email': info['email'],
                'password': "",
                'created_at': info['users.created_at'],
                'updated_at': info['users.updated_at']

            }
            sighting.user= User(row)
            sightings.append(sighting)
        return results
    
    @classmethod
    def add_sighting(cls,data):
        query = """
                INSERT INTO sightings(location, scenario, date_of_sighting, qty_of_sq, created_at, updated_at, user_id)
                VALUES(%(location)s, %(scenario)s, %(date_of_sighting)s, %(qty_of_sq)s,NOW(), NOW(), %(user_id)s); 
                """
        results = connectToMySQL('sasquatch').query_db(query,data)
        return results

    @classmethod
    def getidby(cls,data):
        query = """
                SELECT * FROM sightings
                WHERE id = %(id)s;
                """
        results = connectToMySQL('sasquatch').query_db(query,data)
        return cls(results[0])

    @classmethod
    def update_sightings(cls,data):
        query = """
                UPDATE sightings
                SET location = %(location)s, scenario = %(scenario)s, date_of_sighting = %(date_of_sighting)s, qty_of_sq = %(qty_of_sq)s, updated_at = NOW()
                WHERE id = %(id)s
                """
        results = connectToMySQL('sasquatch').query_db(query,data)
        return results
    
    @staticmethod
    def validate_sighting(sighting_info):
        is_valid = True
        
        if len(sighting_info['location']) < 2:
            flash("Location is needed/Not valid location")
            is_valid = False
        if len(sighting_info['scenario']) < 2:
            flash("Tell us what happened/Not a valid entry")
            is_valid = False
        if sighting_info['qty_of_sq'] == ''  :
            flash("Please tell us how many you saw")
            is_valid = False
        if sighting_info['date_of_sighting'] == ''  :
            flash("Please input a date")
            is_valid = False
        
        return is_valid
    
    @classmethod
    def remove_sighting(cls, data):
        query = """
                DELETE FROM sightings
                WHERE id = %(id)s
                """
        results = connectToMySQL('sasquatch').query_db(query,data)
        return results