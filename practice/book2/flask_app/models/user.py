from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import sighting
class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.sightingid = []

    @classmethod
    def all_author(cls):
        query = """
                SELECT * FROM users;
                """
        results = connectToMySQL('sasquatch2').query_db(query)
        users = []
        for i in results:
            users.append( cls(i) )
        return users
    
    @classmethod
    def authorfave(cls,data):
        query = """
                SELECT * FROM users 
                LEFT JOIN skeptics ON users.id = skeptics.user_id 
                LEFT JOIN sightings on sightings.id = skeptics.sighting_id 
                WHERE users.id = %(id)s;
                """
        results = connectToMySQL('sasquatch2').query_db(query,data)
        users = cls( results[0])
        if not results:
            return None
        for info in results:
            if info['sightings.id'] == None:
                break
            data = {
                "id": info['id'],
                "location": info['location'],
                "scenario": info['scenario'],
                "date_of_sighting": info['date_of_sighting'],
                "qty_of_sq": info['qty_of_sq'],
                "created_at": info['created_at'],
                "updated_at": info['updated_at']
            }
            users.sightingid.append(sighting.Book(data))
        return users

    @classmethod
    def add_author(cls, data):
        query = """
                INSERT INTO users(first_name, last_name, email, password, created_at, updated_at)
                VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());
                """
        results = connectToMySQL('sasquatch2').query_db(query,data)
        return results
    
    @classmethod
    def notfavea(cls, data):
        query = """
                SELECT * FROM users
                WHERE users.id NOT IN (SELECT user_id FROM skeptics WHERE sighting_id = %(id)s);
                """
        results = connectToMySQL('sasquatch2').query_db(query,data)
        users = []
        for i in results:
            users.append( cls(i) )
        return users

    @classmethod
    def faveauthor(cls,data):
        query = """
                INSERT INTO skeptics(user_id, sighting_id) 
                VALUES(%(user_id)s, %(sighting_id)s);
                """
        results = connectToMySQL('sasquatch2').query_db(query,data)
        return results
   
