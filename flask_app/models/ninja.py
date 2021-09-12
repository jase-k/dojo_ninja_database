
from flask_app.config.mysqlconnection import MySQLConnection

db = 'dojos_ninjas_schema'

class Ninja: 
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created = data["created_at"]
        self.updated = data["updated_at"]

    @classmethod
    def addNinja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) Values(%(fname)s, %(lname)s, %(age)s, NOW(), NOW(), %(dojo_id)s)"

        MySQLConnection(db).query_db(query, data)

        return data["dojo_id"]