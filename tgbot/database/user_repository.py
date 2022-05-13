from tgbot.database.db import Database
from tgbot.database.models.user import User


class UserRepository:
    def __init__(self):
        self.db = Database()

    async def create(self, user):
        saved_user = await self.db.create(User, user)
        return saved_user
