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
    # email = request.form.get('email')
    # name = request.form.get('name')
    # json = request.get_json()
    # print(json)
    # email = json.get("email")
    # name = json.get("name")
    new_user = Employee()
    new_user.Email = request.form.get('email', '')
    new_user.Fax = request.form.get('fax', '')
    new_user.Name = request.form.get('name', '')
    new_user.Telephone = request.form.get('telephone', '')
    new_user.Username = request.form.get('username', '')
    new_user.Password = request.form.get('password', '')
    new_user.CompanyId = request.form.get('companyId')
    new_user.PortalId = request.form.get('portalId', '')
    new_user.RoleId = request.form.get('roleId', '')
    new_user.StatusId = request.form.get('statusId', '')
    new_user.save()

    
    

    return jsonify({"id": new_user.id}), 201

@app.route("/cuentas/", endpoint="lista_cuentas", methods=["GET"])
def list_cuentas():
    cuentas = Cuenta.query.order_by(Cuenta.id).all()

    return jsonify({
        "items": [{"id": x.id, "name": x.name, "email": x.email} for x in cuentas]
    })


