from flask import Blueprint

api = Blueprint("api", __name__)

@api.route("/", methods=["GET"])
def ping():
    return "Test"
