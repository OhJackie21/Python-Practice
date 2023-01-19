from flask_app.config.mysqlconnection import connectToMySQL

class Post:
    def __init__(self,data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = """
                INSERT INTO posts(content, created_at, updated_at )
                VALUES (%(content)s, NOW(), NOW())
                """
        