from datetime import datetime

from sqlalchemy import Column, Integer, String, TIMESTAMP

from sqlalchemy.orm import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'bot_user_account'

    user_id = Column(Integer, primary_key=True)
    first_name = Column(String(30), nullable=True)
    last_name = Column(String(30), nullable=True)
    username = Column(String(50), nullable=True)
    phone = Column(String(15), index=True)
    registered = Column(TIMESTAMP(timezone=False), default=datetime.now(), index=True)

    def __repr__(self):
        return f'{self.first_name} {self.last_name}, {self.phone}'
