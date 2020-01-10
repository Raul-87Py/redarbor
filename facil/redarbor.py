from api import app
from api import db
from api import routes

if __name__ == "__main__":
    db.create_all() # Creamos todas las tablas de la base de datos    
    app.run(port=3700, host="0.0.0.0", debug=True)