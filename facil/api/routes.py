from.models import EmployeeModel
from . import app
from .utilities import  response_helper, cooking_datas, get_dict

from flask import request
from flask import jsonify, make_response


 
@app.route("/api/redarbor/", methods=["POST"])
def new_employee():
    """add new user
    
    Returns:
        id -- database id to new element
    """
    try:
        new_user = EmployeeModel(dict(request.form))
        id = new_user.add_data() 
        response = response_helper(True, msg="SUCCES", data={'ID':id})
        
    except Exception as e:
        app.logger.error(e)
        response = response_helper(False, msg="ERROR", error=str(e))

    return response


@app.route("/api/redarbor/", methods=["GET"])
def list_exployeers():
    try:
        data = EmployeeModel.get_all() 
        employeers = cooking_datas(data)
        response = response_helper(True, msg="Employers Data", data=employeers)
        
    except Exception as e:
        app.logger.error(e)
        response = response_helper(False, msg="ERROR", error=str(e))

    return response

@app.route("/api/redarbor/<id>", methods=["GET"])
def one_exployee(id):
    
    try:
        data = EmployeeModel.get_by_id(id)
        employee = get_dict(data)
        response = response_helper(True, msg="Employee Data", data=employee)
        
    except Exception as e:
        app.logger.error(e)
        response = response_helper(False, msg="ERROR", error=str(e))

    return response

@app.route("/api/redarbor/<id>", methods=["PUT"])
def update_exployee(id):
    try:
        new_values = dict(request.form)
        EmployeeModel.update_by_id(id, new_values) 
        response = response_helper(True, msg="SUCCES")
        
    except Exception as e:
        app.logger.error(e)
        response = response_helper(False, msg="ERROR", error=str(e))

    return response

@app.route("/api/redarbor/<id>", methods=["DELETE"])
def delete_exployee(id):
    try:
        EmployeeModel.delete_by_id(id) 
        response = response_helper(True, msg="SUCCES")
        
    except Exception as e:
        app.logger.error(e)
        response = response_helper(False, msg="ERROR", error=str(e))

    return response

