import requests
from aiogram import Dispatcher
from requests.auth import HTTPBasicAuth
from aiogram.types import Message

from tgbot.database.models.user import User
from tgbot.middlewares.db import check_user

ALLIO_SERVER_URL = 'https://dev.allio.ru/allio/api/lpc/v1/'


@check_user()
async def get_all_kp(message: Message, user: User):
    data = {}
    r = requests.post(ALLIO_SERVER_URL, data=data, auth=HTTPBasicAuth('user', 'password'))
    # TODO: авторизац. токены, url в .env и конфиг
    # TODO: сформировать запрос и примерный вывод ответа из большого json`a (в misc или services модуль BEAUTIFY)


def register_side_service(dp: Dispatcher):
    dp.register_message_handler(get_all_kp, commands=['get_kp'], state='*')
