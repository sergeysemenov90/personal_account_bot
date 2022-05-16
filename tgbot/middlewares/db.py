from aiogram import types
from aiogram.dispatcher.handler import CancelHandler, current_handler
from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware, BaseMiddleware

from tgbot.database.user_repository import UserRepository
from tgbot.keyboards.reply import contact_request_kb


def check_user(check=True):

    def decorator(func):
        if check:
            setattr(func, 'check_user_in_db', True)
        return func

    return decorator


class DbMiddleware(LifetimeControllerMiddleware):
    skip_patterns = ["error", "update"]

    async def pre_process(self, obj, data, *args):
        db_session = obj.bot.get('db')
        # Передаем данные из таблицы в хендлер
        # data['some_model'] = await Model.get()


class SavedInDbMiddleware(BaseMiddleware):
    """
    Поиск юзера в БД для предоставления доступа к некоторым хэндлерам
    Для добавления ограничения для хэндлера вешается декоратор check_user
    """
    def __init__(self):
        super(SavedInDbMiddleware, self).__init__()

    async def on_process_message(self, message: types.Message, data: dict):
        handler = current_handler.get()
        if getattr(handler, 'check_user_in_db', False):
            user_id = message.from_user.id
            user = await UserRepository().get(user_id)

            if not user:
                await message.answer('Чтобы пользоваться функцией, нужно поделиться своим контактом',
                                     reply_markup=contact_request_kb)
                raise CancelHandler()
            data['user'] = user
