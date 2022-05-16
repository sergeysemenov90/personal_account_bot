from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from tgbot.config import load_config
from tgbot.database.models.user import Base


class Database:
    """Подключение и работа с базой данных"""
    def __init__(self):
        self.config = load_config('.env')
        self.engine = None

    async def make_engine(self):
        db_config = self.config.db
        engine = create_async_engine(f'mysql+aiomysql://{db_config.user}:'
                                     f'{db_config.password}@'
                                     f'{db_config.host}:'
                                     f'{db_config.port}/'
                                     f'{db_config.database}')
        return engine

    async def base_metadata_save(self):
        engine = await self.make_engine()
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

        async_session = sessionmaker(
            engine, expire_on_commit=False, class_=AsyncSession
        )
        return async_session

    async def create(self, model, obj):
        async_session = await self.base_metadata_save()
        obj_to_create = model(**obj.__dict__)
        async with async_session() as session:
            async with session.begin():
                session.add(obj_to_create)
                await session.commit()
                return obj_to_create

    async def get(self, model, id):
        async_session = await self.base_metadata_save()
        async with async_session() as session:
            async with session.begin():
                result = await session.execute(select(model).where(model.user_id == id))
                user = result.scalars().first()
                return user


