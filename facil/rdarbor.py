from redarbor import app
from redarbor import db

if __name__ == "__main__":
     # Creamos todas las tablas de la base de datos
    
    from redarbor import routes
    db.create_all()
    app.run(port=3700, host="0.0.0.0", debug=True)