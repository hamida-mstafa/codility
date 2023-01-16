import flask
from flask import request
import json
import traceback

from save import save


app = flask.Flask(_name_)


@app.route("/users", methods=["POST"])
def users():
    r_content = request.get_json()
    r_json = json.loads(r_content)
    try:
        name, age = r_json["name"], r_json["age"]
    except KeyError:
        return flask.jsonify(message={}, status=400), 400
    
    if len(name) > 32:
        return flask.jsonify(message={}, status=400), 400
    
    if not type(age) is int:
        return flask.jsonify(message={}, status=400), 400
    
    if age < 16:
        return flask.jsonify(message={}, status=400), 400
    
    response = save(r_json)
    return flask.jsonify(message=response, status=201), 201


if _name_ == "_main_":
    app.run()