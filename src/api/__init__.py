from flask import Blueprint
from flask_restx import Api

from .user.endpoints import api as user_api

blueprint = Blueprint("api", __name__)

authorizations = {
    "Authorization": {
        "description": "",
        "type": "apiKey",
        "in": "header",
        "name": "Authorization",
    }
}

api = Api(
    blueprint,
    title="Flask Boilerplate API",
    version="0.1",
    description="Flask Boilerplate APIs",
    authorizations=authorizations,
    security="Authorization",
)

api.add_namespace(user_api)
