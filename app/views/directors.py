from flask_restx import Resource, Namespace

from app.dao.model.director import DirectorSchema
from app.implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        """Представление возвращает всех режиссёров"""
        rs = director_service.get_all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200


@director_ns.route('/<int:uid>')
class DirectorView(Resource):
    def get(self, uid):
        """Представление возвращает режиссёра по id"""
        r = director_service.get_one(uid)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200
