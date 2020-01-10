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
    """add new user
    
    Returns:
        id -- database id to new element
    """
    new_user = Employee(dict(request.form))
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
    employee = Employee.update_by_id(id, new_values)
    #TODO return ok 200

@app.route("/api/redarbor/<id>", methods=["DELETE"])
def delete_exployee(id):
    #TODO return ok 200
    employee = Employee.delete_by_id(id)
    # return jsonify('200')
