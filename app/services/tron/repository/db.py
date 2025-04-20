from fastapi import Depends
from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import async_sessionmaker

from app.db import get_sessionmaker
from app.services.tron.repository.base import AbstractRepository
from app.services.tron.models import Account
from app.services.tron.schemas import TronAddressResponse


class DBRepository(AbstractRepository):
    session: async_sessionmaker

    @classmethod
    async def get_all(cls, offset: int, limit: int) -> list[Account]:
        async with cls.session() as session:
            query = (
                select(Account)
                .order_by(desc(Account.id))
                .offset(offset)
                .limit(limit)
            )
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def get_by_address(cls, address: str, offset: int, limit: int) -> list[Account]:
        async with cls.session() as session:
            query = (
                select(Account)
                .where(Account.address == address)
                .order_by(desc(Account.id))
                .offset(offset)
                .limit(limit)
            )
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def create(cls, account: TronAddressResponse) -> Account:
        async with cls.session() as session:
            instance = Account(**account.model_dump())
            session.add(instance)
            await session.commit()
            return instance


def get_repository(session: async_sessionmaker = Depends(get_sessionmaker)):
    repo = DBRepository
    repo.session = session

    return repo
