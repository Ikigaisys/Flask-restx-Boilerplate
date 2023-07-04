from flask import g, request
from werkzeug.exceptions import Unauthorized

from config import settings
from model.user import User


def auth(value: str):
    """
    Authorize user

    Args:
        value: Permission to check if used as @auth(PERMISSION) otherwise callable

    Raises:
        Unauthorized: Authorization Missing, Invalid Token or Unauthorized user

    Returns:
        Decorated function
    """

    def wraps(f):
        def wrapper_function(*args, **kwargs):
            g.user = None
            authorization = request.headers.get("Authorization")
            env = settings.env
            if not authorization:
                err = {"status": "nok", "errors": ["Authorization Missing."]}
                raise Unauthorized(err)
            if authorization.startswith("Basic ") and env in ["dev", "testing"]:
                email = authorization.split("Basic ")[1]
                g.user = User.get_by_email(email)
            else:
                token = authorization.split("Bearer ")
                if token and len(token) == 2:
                    token = token[1]
                else:
                    raise Unauthorized({"status": "nok", "errors": ["Invalid Token."]})
                # Decode and validate tokens here, like JWTs
                # Set g.user if a user is found and the token is valid
            if g.user:
                # "Permission" from the parameter can be used here and checked in
                # a "RolePermission" table to ensure that only a "User" with
                # sufficient permissions can access the endpoint, otherwise throw forbidden.
                return f(*args, **kwargs)
            raise Unauthorized({"status": "nok", "errors": ["Unauthorized user."]})

        return wrapper_function

    if hasattr(value, "__call__"):
        f = value
        value = None
        return wraps(f)

    return wraps
