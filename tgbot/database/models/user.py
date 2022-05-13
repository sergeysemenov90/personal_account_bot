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
    phone = Column(Integer, index=True)
    registered = Column(TIMESTAMP(timezone=False), default=datetime.now(), index=True)
