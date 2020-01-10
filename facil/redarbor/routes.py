from .models import Employee
from . import app
from flask import request, jsonify
 

@app.route("/")
def server_info():
    return jsonify({
        "server": "My API"
    })

@app.route("/api/redarbor/", methods=["POST"])
def new_account():
    # email = request.form.get('email')
    # name = request.form.get('name')
    # json = request.get_json()
    # print(json)
    # email = json.get("email")
    # name = json.get("name")
    new_user = Employee(dict(request.form))
    # new_user.Email = request.form.get('email', '')
    # new_user.Fax = request.form.get('fax', '')
    # new_user.Name = request.form.get('name', '')
    # new_user.Telephone = request.form.get('telephone', '')
    # new_user.Username = request.form.get('username', '')
    # new_user.Password = request.form.get('password', '')
    # new_user.CompanyId = request.form.get('companyId')
    # new_user.PortalId = request.form.get('portalId', '')
    # new_user.RoleId = request.form.get('roleId', '')
    # new_user.StatusId = request.form.get('statusId', '')
    new_user.save()

    
    

    return jsonify({"id": new_user.id}), 201

@app.route("/api/redarbor/", methods=["GET"])
def list_exployeers():
    employee = Employee.get_all()

    return jsonify({
        "Employeers": [{"id": x.id, "Name": x.Name, "Email": x.Email} for x in employee]
    })

@app.route("/api/redarbor/<id>", methods=["GET"])
def one_exployee(id):
    employee = Employee.get_by_id(id)
    return jsonify({
        "item": {"id": employee.id, "Name": employee.Name, "Email": employee.Email}
    })

@app.route("/api/redarbor/<id>", methods=["PUT"])
def update_exployee(id):
    new_values = dict(request.form)
    employee = Employee.query.get(id)
    return jsonify({
        "item": {"id": employee.id, "Name": employee.Name, "Email": employee.Email}
    })
