from flask import jsonify

def response_helper(result=True, msg="", error="", data={}, error_code=400):
    """
    Simple formatter for rest responses.

    Args:
        result: bol.
        error: str.
        data: dict.
    """

    if not isinstance(result, bool):
        raise TypeError

    if not isinstance(msg, str):
        raise TypeError

    # if not isinstance(data, dict):
    #     raise TypeError

    if not isinstance(error, str) and not isinstance(error, bool):
        raise TypeError

    if not isinstance(error_code, int):
        raise TypeError

    if error_code < 100 or error_code > 520:  # Fast check of error codes
        raise WrongArgsError

    if result:
        return jsonify(
            {
                "result": result,
                "error": error,
                "msg": msg,
                "data": data
            }
        ), 200
    else:
        return jsonify(
            {
                "result": result,
                "error": error,
                "msg": msg,
                "data": data
            }
        ), error_code

def cooking_datas(employeers):
    data = {"Employeers":[]}
    for employee in employeers:
        new_dict = get_dict(employee)
        data["Employeers"].append(new_dict)
    return data

def get_dict(employee):
    new_dict = employee.__dict__
    del new_dict['_sa_instance_state'] # delete specific
    return new_dict