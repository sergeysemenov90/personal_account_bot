import logging

from aiogram import Dispatcher
from aiogram.types import Message, ChatActions, ReplyKeyboardRemove
import asyncio

from tgbot.database.user_repository import UserRepository
from tgbot.keyboards import reply
from tgbot.models.user import User


async def user_start(message: Message):
    await message.bot.send_chat_action(message.chat.id, ChatActions.TYPING)
    await message.answer("Привет! Это бот-помощник Allio\nОн может предоставить тебе данные твоего личного кабинета"
                         "\nПожалуйста, поделись своим номером. Он необходим для поиска в Allio",
                         reply_markup=reply.contact_request_kb)


async def user_contact_save(message: Message):
    await message.answer(f'Спасибо! Ваш номер телефона - {message.contact.phone_number}\n'
                         f'Ваше имя - {message.contact.first_name}', reply_markup=ReplyKeyboardRemove())
    await message.bot.send_chat_action(message.chat.id, ChatActions.TYPING)
    user = User(user_id=message.from_user.id,
                first_name=message.contact.first_name,
                last_name=message.contact.last_name,
                username=message.from_user.username,
                phone=message.contact.phone_number[2:])
    repo = UserRepository()
    saved_user = await repo.create(user)
    logger = logging.getLogger()
    logger.info(saved_user)
    await message.answer('Ищем вас в базе данных...')
    await message.bot.send_chat_action(message.chat.id, ChatActions.TYPING)
    await asyncio.sleep(2)
    await message.answer('Спасибо! Теперь вы имеете доступ к данным allio')


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_message_handler(user_contact_save, content_types=['contact', ], state="*")
