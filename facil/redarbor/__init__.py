from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import request

app = Flask(__name__)
#postgresql://<nombre_usuario>:<password>@<host>:<puerto>/<nombre_basededatos>
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:secret@127.0.0.1:33060/demo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

