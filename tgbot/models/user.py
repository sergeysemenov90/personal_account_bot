from datetime import datetime
from dataclasses import dataclass


@dataclass()
class User:
    user_id: int
    first_name: str
    last_name: str
    username: str
    phone: str
    registered: datetime = None

    def __str__(self):
        return f'{self.__class__.__name__}: {self.user_id}, {self.username}'


