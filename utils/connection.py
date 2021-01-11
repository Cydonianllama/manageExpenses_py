from pymongo import MongoClient
class connection:
    client = MongoClient('mongodb://localhost:27017/')
    def __init__(self,userdb,hostname,dbname,password):
        self.hostname = hostname
        self.userdb = userdb
        self.dbname = dbname
        self.password = password
    def __init__(self):
        print('hello mongo db')
    def getClient(self):
        return self.client
Mongo = connection()
db = Mongo.getClient().testDB
