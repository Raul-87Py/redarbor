import logging
from logging.handlers import RotatingFileHandler
from flask.logging import default_handler

from api import app
from api import db
from api import routes
from api.conf import PORT, HOST

if __name__ == "__main__":
    try:
        #TODO stting logging
        logging.basicConfig(filename='api/logs/app.log', level=logging.DEBUG, format="%(asctime)s %(levelname)s %(name)s : %(message)s")
        db.create_all() # Creamos todas las tablas de la base de datos    
        app.run(port=PORT, host=HOST, debug=True)
    except Exception as e:
        app.logger.error(e)
