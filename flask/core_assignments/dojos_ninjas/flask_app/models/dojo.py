from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data['first_name']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
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
        query = "INSERT INTO dojos (name) VALUES (%(name)s); "
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        return results
    
    @classmethod
    def ninjas_in_dojo(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        return cls(results[0])
