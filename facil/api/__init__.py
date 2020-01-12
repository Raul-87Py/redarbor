from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

from .conf import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)
#postgresql://<nombre_usuario>:<password>@<host>:<puerto>/<nombre_basededatos>
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# f"{db_conf['db']}://{db_conf['nombre_usuario']}:{db_conf['password']}@ \
#         {db_conf['host']}:{db_conf['puerto']}/{db_conf['nombre_basededatos']}"