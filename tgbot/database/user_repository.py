from tgbot.database.db import Database
from tgbot.database.models.user import User


class UserRepository:
    def __init__(self):
        self.db = Database()
        self.model = User

    async def create(self, user):
        saved_user = await self.db.create(self.model, user)
        return saved_user

    async def get(self, user_id):
        user = await self.db.get(self.model, user_id)
        return user
