import calendar
import datetime

import jwt

from constants import SECRET, ALGORITHM
from dao.model.user import UserSchema


def generate_jwt(user_obj):
    """
    Функция, которая генерирует access_token и refresh_token, аргумент функция принимает словарь вида user_obj
    В access и в refresh токене содержиться информация об: имени пользователя ('username'), роли ('role')
    и времени действия токена ('exp')
    """
    data = UserSchema().dump(user_obj)

    min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    data["exp"] = calendar.timegm(min30.timetuple())
    access_token = jwt.encode(data, SECRET, algorithm=ALGORITHM)
    days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
    data["exp"] = calendar.timegm(days130.timetuple())
    refresh_token = jwt.encode(data, SECRET, algorithm=ALGORITHM)
    return {"access_token": access_token, "refresh_token": refresh_token}
