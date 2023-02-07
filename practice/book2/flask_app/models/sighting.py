from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user


class Sighting:
    def __init__(self, data):
        self.id = data['id']
        self.location = data['location']
        self.scenario = data['scenario']
        self.date_of_sighting = data['date_of_sighting']
        self.qty_of_sq = data['qty_of_sq']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.userid = []
        
    
    @classmethod
    def all_boooks(cls):
        query = "SELECT * FROM sightings;"
        results = connectToMySQL('sasquatch2').query_db(query)
        sightings = []
        for i in results:
            sightings.append( cls(i) )
        return sightings

    @classmethod
    def bookfaves(cls,data):
        query = """
                SELECT * FROM sightings 
                LEFT JOIN skeptics ON sightings.id = skeptics.sighting_id 
                LEFT JOIN users ON users.id = skeptics.user_id 
                WHERE sightings.id = %(id)s;
                """
        results = connectToMySQL('sasquatch2').query_db(query,data)
        sightings = cls( results[0])
        for st in results:
            if st['users.id'] == None:
                break
            data = {
                "id": st['users.id'],
                "first_name": st['first_name'],
                "last_name": st['last_name'],
                "email": st['email'],
                "password": "",
                "created_at": st['created_at'],
                "updated_at": st['updated_at']
            }
            sightings.userid.append(user.User(data))
        return sightings
    
    @classmethod
    def notfaveb(cls, data):
        query = """
                SELECT * FROM sightings 
                WHERE sightings.id NOT IN (SELECT sighting_id FROM skeptics WHERE user_id = %(id)s);
                """
        results = connectToMySQL('sasquatch2').query_db(query,data)
        sightings = []
        for i in results:
            sightings.append( cls(i) )
        return sightings
    
    @classmethod
    def favebook(cls,data):
        query = """
                INSERT INTO skeptics(user_id, sighting_id) 
                VALUES(%(user_id)s, %(sighting_id)s);
                """
        results = connectToMySQL('sasquatch2').query_db(query,data)
        return results

    @classmethod
    def addbook(cls,data):
        query = """
                INSERT INTO sightings(location, scenario, date_of_sighting, qty_of_sq, created_at, updated_at)
                VALUES(%(location)s, %(scenario)s, %(date_of_sighting)s, %(qty_of_sq)s,NOW(), NOW()); 
                """
        results = connectToMySQL('sasquatch2').query_db(query,data)
        return results