from flask_pymongo import PyMongo
from src import app



class DataBase:
    def __init__(self, uri, db):
        self.uri = uri
        self.db = db

    def connect(self):
        self.connection = PyMongo(self.uri)
        return self.connection

    def getDb(self):
        return self.connection[self.db]

