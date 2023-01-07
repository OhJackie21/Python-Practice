from flask_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos; "
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for i in results:
            dojos.append( cls(i) )
        return dojos

    @classmethod
    def add(cls, data):
        query = "INSERT INTO dojos(name) VALUES (%(name)s); "
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return results
    
    @classmethod
    def ninjas_in_dojo(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        print(results)
        dojo = cls(results[0])
        for info in results:
            all = {
                'id': info['ninjas.id'],
                'first_name': info['first_name'],
                'last_name': info['last_name'],
                'age': info['age'],
                'created_at': info['created_at'],
                'updated_at': info['updated_at'],
                'dojo_id': info['dojo_id']
            }
            dojo.ninjas.append( Ninja(all))
        return dojo

