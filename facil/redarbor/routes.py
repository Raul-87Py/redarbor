from .models import Employee
from . import app
from flask import request, jsonify
 

@app.route("/")
def server_info():
    return jsonify({
        "server": "My API"
    })

@app.route("/cuentas/", endpoint="nueva_cuenta", methods=["POST"])
def new_account():
    email = request.form.get('email')
    name = request.form.get('name')
    # json = request.get_json()
    # print(json)
    # email = json.get("email")
    # name = json.get("name")
    print('poop',dict(request.form),'pop')
    new_user = Employee(dict(request.form))
    new_user.insert()

    
    

    return jsonify({"id": new_user.id}), 201

@app.route("/cuentas/", endpoint="lista_cuentas", methods=["GET"])
def list_cuentas():
    cuentas = Cuenta.query.order_by(Cuenta.id).all()

    return jsonify({
        "items": [{"id": x.id, "name": x.name, "email": x.email} for x in cuentas]
    })


