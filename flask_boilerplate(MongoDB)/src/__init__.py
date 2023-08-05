from flask import Flask
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config["SECRET_KEY"] = 'random'
app.config["MONGO_URI"] = 'dbUrl'

# Mongodb setup
# mongodb_client = PyMongo(app)
# db = mongodb_client.db

from src.db.connection import DataBase

DataBase()
from src.models.users import User
from src.routes import app_route
