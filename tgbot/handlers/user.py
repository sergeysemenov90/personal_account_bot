import logging

from aiogram import Dispatcher
from aiogram.types import Message, ChatActions, ReplyKeyboardRemove

from tgbot.database.user_repository import UserRepository
from tgbot.keyboards import reply, inline
from tgbot.models.user import User


async def user_start(message: Message):
    await message.bot.send_chat_action(message.chat.id, ChatActions.TYPING)
    await message.answer("Привет! Это бот-помощник Allio\nОн может предоставить тебе данные твоего личного кабинета"
                         "\nПожалуйста, поделись своим номером. Он необходим для поиска в Allio",
                         reply_markup=reply.contact_request_kb)


async def user_contact_save(message: Message):
    await message.answer(f'Спасибо, {message.contact.first_name}! Вы можете начать работать с системой',
                         reply_markup=reply.all_func_kb)
    user = User(user_id=message.from_user.id,
                first_name=message.contact.first_name,
                last_name=message.contact.last_name,
                username=message.from_user.username,
                phone=message.contact.phone_number[2:])
    repo = UserRepository()
    await repo.create(user)


async def user_get(message: Message):
    user: User = await UserRepository().get(message.from_user.id)
    if user:
        await message.answer(f'Вы - {user.first_name} {user.last_name}')
    else:
        await message.answer('Вы не сохранены в БД')


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_message_handler(user_contact_save, content_types=['contact', ], state="*")
    dp.register_message_handler(user_get, commands=['me'], state="*")
