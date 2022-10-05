import os
from pickle import FALSE
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from .model import User
import sys 

sys.path.append("C:\\Users\\drago\\OneDrive\\Documents\\devMoutain\\specilzationCapstone")


app = Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'SQLITE:///' +os.path.join(basedir,'data.sqlite')

app.config['SQLACHELMY_TRACK_MODIFICATIONS'] = FALSE

db = SQLAlchemy(app)
Migrate(app,db)

