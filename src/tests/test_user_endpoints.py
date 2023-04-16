from http import HTTPStatus
from unittest.mock import ANY


def test_user_post(client, post):
    user_post = {"username": "py", "email": "test@test.com"}
    user_post_response = {
        "status": "ok",
        "data": {
            "id": ANY,
            "username": "py",
            "email": "test@test.com",
            "created_at": ANY,
        },
    }
    resp = post(client, f"user", user_post)
    assert resp.json() == user_post_response
    assert resp.status_code == HTTPStatus.CREATED


def test_user_get(client, get):
    user_get = {
        "status": "ok",
        "data": [
            {"id": ANY, "username": "py", "email": "test@test.com", "created_at": ANY}
        ],
    }
    resp = get(client, "user")
    assert resp.json() == user_get
    assert resp.status_code == HTTPStatus.OK
