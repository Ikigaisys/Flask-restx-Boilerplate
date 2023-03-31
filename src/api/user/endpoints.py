from http import HTTPStatus
from typing import Dict, Tuple

from flask_restx import Resource

from api.user import schemas
from helpers.api import auth
from model.user import User

from . import api


@api.route("")
class UserList(Resource):
    @api.doc("Add new user")
    @api.expect(schemas.user_expect, validate=True)
    @api.marshal_list_with(schemas.user_response, skip_none=True)
    def post(self) -> Tuple[Dict, int]:
        """
        Add new user

        Returns:
            User
        """
        api.logger.info("Create user")
        user = User.get_by_email(api.payload["email"])
        if user:
            response = {"status": "nok", "errors": ["User already exists."]}
            return response, HTTPStatus.BAD_REQUEST

        user = User(**api.payload).insert()
        return {"status": "ok", "data": user}, HTTPStatus.CREATED

    @api.doc("List users")
    @api.marshal_list_with(schemas.user_list_response, skip_none=True)
    def get(self) -> Tuple[Dict, int]:
        """
        Get all users

        Returns:
            List of users
        """
        api.logger.info("List users")
        users = User.get()
        return {"status": "ok", "data": users}, HTTPStatus.OK


@api.route("/<int:user_id>")
class UserItem(Resource):
    @api.doc("Get user by id")
    @api.marshal_list_with(schemas.user_response, skip_none=True)
    def get(self, user_id: int) -> Tuple[Dict, int]:
        """
        Get user by id

        Args:
            user_id: user id

        Returns:
            User
        """
        api.logger.info("Get user by id")
        user = User.get_by_id(user_id)
        if not user:
            response = {"status": "nok", "errors": ["User does not exist."]}
            return response, HTTPStatus.NOT_FOUND
        return {"status": "ok", "data": user}, HTTPStatus.OK

    @api.doc("Delete user")
    @auth
    def delete(self, user_id: int) -> Tuple[dict, int]:
        """
        Delete user

        Returns:
            Failure or 204
        """
        api.logger.info("Delete user")
        user = User.get_by_id(user_id)
        if not user:
            response = {"status": "nok", "errors": ["User does not exist."]}
            return response, HTTPStatus.NOT_FOUND
        user.delete()
        return "", HTTPStatus.NO_CONTENT