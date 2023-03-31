from flask_restx.fields import Integer, List, Nested, String

from . import api

user = api.model(
    "user",
    {
        "id": Integer(),
        "username": String(),
        "email": String(),
        "created_at": String(),
    },
)

user_expect = api.model(
    "user_expert",
    {
        "username": String(),
        "email": String(),
    },
)

user_response = api.model(
    "user_response",
    {
        "status": String(description="ok|nok"),
        "data": Nested(user, skip_none=True, allow_null=True),
        "errors": List(String),
    },
)

user_list_response = api.model(
    "user_list_response",
    {
        "status": String(description="ok|nok"),
        "data": Nested(user, skip_none=True, allow_null=True, as_list=True),
        "errors": List(String),
    },
)
