from flask_app.models.ninja import Ninja
from flask_app.config.mysqlconnection import MySQLConnection

db = 'dojos_ninjas_schema'

class Dojo: 
    def __init__(self, data):
        self.id = data['id']
        self.name = data["name"]
        self.created = data['created_at']
        self.lastUpdate = data['updated_at']

        self.ninjas = []

    @classmethod
    def getAllDojos(cls):
        query = "SELECT * from dojos"

        return MySQLConnection(db).query_db(query)

    @classmethod
    def addDojo(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) Values(%(name)s, NOW(), NOW())"
        info = {
            "name" : data['name']
        }
        return MySQLConnection(db).query_db(query, info)


    @classmethod
    def getDojoById(cls, id):
        query = "SELECT * from dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s"
        data = {
            "id" : id
        }
        
        results = MySQLConnection(db).query_db(query, data)
        print("Results of DojoByID: ", results)

        print("First ROW: ", results[0])

        dojo = cls(results[0])
        
        for row in results:
            data = {
                "id" : row["ninjas.id"], 
                "first_name" : row["first_name"],
                "last_name" : row["last_name"],
                "age" : row["age"],
                "created_at" : row["created_at"],
                "updated_at" : row["updated_at"]
            }
            dojo.ninjas.append(Ninja(data))

        # print("Dojo from id: ", dojo)

        return dojo