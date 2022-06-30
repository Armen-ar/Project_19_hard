import hashlib

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        """Метод возвращает пользователя по id"""
        return self.dao.get_one(uid)

    def get_by_username(self, username):
        """Метод возвращает пользователя по имени"""
        return self.dao.get_by_username(username)

    def get_all(self):
        """Метод возвращает всех пользователей"""
        return self.dao.get_all()

    def create(self, user_data):
        """Метод добавляет нового пользователя с хэшированным паролем"""
        user_data["password"] = self.get_hash(user_data["password"])
        return self.dao.create(user_data)

    def delete(self, uid):
        """Метод удаляет пользователя по id"""
        return self.dao.delete(uid)

    def update(self, user_data):
        """Метод обновления данных пользователя с хэшированным паролем"""
        user_data["password"] = self.get_hash(user_data["password"])
        self.dao.update(user_data)
        return self.dao

    def get_hash(self, password):
        """Метод хеширование пароля"""

        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ).decode("utf-8", "ignore")
