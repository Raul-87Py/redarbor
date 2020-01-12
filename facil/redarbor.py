import logging
from logging.handlers import RotatingFileHandler
from flask.logging import default_handler

from api import app
from api import db
from api import routes
from api.conf import PORT, HOST

if __name__ == "__main__":
    logging.basicConfig(filename='app.log', level=logging.DEBUG, format="%(asctime)s %(levelname)s %(name)s : %(message)s")
    db.create_all() # Creamos todas las tablas de la base de datos    
    app.run(port=PORT, host=HOST, debug=True)
