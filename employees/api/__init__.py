from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

from .conf import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
