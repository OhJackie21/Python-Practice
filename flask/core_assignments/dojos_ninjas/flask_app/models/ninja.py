from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
    
    
    @classmethod
    def addninja(cls, data):
        query = "INSERT INTO ninjas(first_name, last_name, age, dojo_id, created_at, updated_at ) VALUES(%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW(), NOW());"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return results

    @classmethod
    def update(cls,data):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s, dojo_id = %(dojo_id)s, updated_at = NOW() WHERE id = %(ids)s"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return results
    
    @classmethod
    def delete_ninja(cls,data):
        query = "DELETE FROM ninjas WHERE id = %(id)s"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return results

    @classmethod
    def ninja_info(cls,data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        print(results)
        return cls(results[0])