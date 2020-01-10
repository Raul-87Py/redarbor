from .models import Employee
from . import app
from .utilities import cooking_datas, get_dict

from flask import request
from flask import jsonify, make_response


 
@app.route("/api/redarbor/", methods=["POST"])
def new_account():
    """add new user
    
    Returns:
        id -- database id to new element
    """
    new_user = Employee(dict(request.form))
    new_user.add()
    data = {'message': 'Created', 'code': 'SUCCESS', "id": new_user.id }
    return make_response(jsonify(data), 200)


@app.route("/api/redarbor/", methods=["GET"])
def list_exployeers():
    employeers = Employee.get_all()   
    data = cooking_data(employeers) 
    return make_response(data, 200)

@app.route("/api/redarbor/<id>", methods=["GET"])
def one_exployee(id):
    employee = Employee.get_by_id(id)
    data = get_dict(employee) 
    return make_response(data, 200)

@app.route("/api/redarbor/<id>", methods=["PUT"])
def update_exployee(id):
    new_values = dict(request.form)
    result = Employee.update_by_id(id, new_values)
    return result

@app.route("/api/redarbor/<id>", methods=["DELETE"])
def delete_exployee(id):
    result = Employee.delete_by_id(id)
    return result
