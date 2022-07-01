from flask_restx import Resource, Namespace

from app.dao.model.genre import GenreSchema
from app.implemented import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        """Представление возвращает все жанры"""
        rs = genre_service.get_all()
        res = GenreSchema(many=True).dump(rs)
        return res, 200


@genre_ns.route('/<int:uid>')
class GenreView(Resource):
    def get(self, uid):
        """Представление возвращает жанр по id"""
        r = genre_service.get_one(uid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200
