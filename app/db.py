from fastapi.params import Depends
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.core.config import get_db_url


def get_sessionmaker(db_url: str = Depends(get_db_url)) -> async_sessionmaker:
    engine = create_async_engine(db_url)
    session_maker = async_sessionmaker(engine, expire_on_commit=False)
    return session_maker
