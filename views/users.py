from flask import request
from flask_restx import Namespace, Resource

from dao.model.user import UserSchema
from implemented import user_service

user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        """Представление возвращает всех пользователей"""
        users = user_service.get_all()
        response = UserSchema(many=True).dump(users)

        return response, 200

    def post(self):
        """Представление добавляет нового пользователя"""
        data = request.json
        user = user_service.create(data)

        return "", 201, {"location": f"/users/{user.id}"}


@user_ns.route('/<int:uid>')
class UserView(Resource):
    def delete(self, uid):
        """Представление удаляет пользователя по id"""
        user_service.delete(uid)

        return "", 204
