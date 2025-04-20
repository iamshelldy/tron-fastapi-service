from abc import ABC, abstractmethod
from inspect import currentframe
from typing import TypeVar, Generic

from app.services.tron.schemas import TronAddressResponse

T = TypeVar("T")


class AbstractRepository(ABC, Generic[T]):
    @classmethod
    @abstractmethod
    async def get_all(cls, offset: int, limit: int) -> list[T]:
        raise NotImplementedError(f"`{cls.__name__}` must define method "
                                  f"`{currentframe().f_code.co_name}()`.")

    @classmethod
    @abstractmethod
    async def get_by_address(cls, address: str, offset: int, limit: int) -> list[T]:
        raise NotImplementedError(f"`{cls.__name__}` must define method "
                                  f"`{currentframe().f_code.co_name}()`.")

    @classmethod
    @abstractmethod
    async def create(cls, account: TronAddressResponse) -> T:
        raise NotImplementedError(f"`{cls.__name__}` must define method "
                                  f"`{currentframe().f_code.co_name}()`.")
