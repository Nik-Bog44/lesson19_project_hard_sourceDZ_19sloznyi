from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from implemented import user_service

user_ns = Namespace('users')


@user_ns.route('/')
class GenresView(Resource):
    def get(self):
        users = user_service.get_all()
        res = UserSchema(many=True).dump(users)
        return res, 200

    def post(self):
        req_json = request.json
        user = user_service.create(req_json)
        return "", 201, {"location": f"/user/{user.id}"}


@user_ns.route('/<int:rid>')
class GenreView(Resource):
    def get(self, uid):
        user = user_service.get_one(uid)
        sm_d = UserSchema().dump(user)
        return sm_d, 200

    def put(self, uid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = uid
            user_service.update(req_json)
            return "", 204

    def delete(self, uid):
        user_service.delete(uid)
        return "", 204
