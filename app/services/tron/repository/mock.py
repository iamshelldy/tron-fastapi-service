import string
from datetime import datetime

from random import randint, random, choice

from app.services.tron.repository.base import AbstractRepository
from app.services.tron.schemas import TronAddressResponse


def generate_random_address() -> str:
    alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return "".join(choice(alphabet) for _ in range(34))


def generate_random_account() -> TronAddressResponse:
    return TronAddressResponse(
        address=generate_random_address(),
        created_at=datetime.now(),
        balance=10_000 * random(),
        bandwidth=randint(0, 600),
        energy=randint(0, 600),
    )


def generate_random_repo_data(length: int) -> list[TronAddressResponse]:
    return [generate_random_account() for _ in range(length)]


class MockRepository(AbstractRepository[TronAddressResponse]):
    __data = generate_random_repo_data(100)

    @classmethod
    async def get_all(cls, offset: int, limit: int) -> list[TronAddressResponse]:
        end = min(offset + limit, len(cls.__data))
        return cls.__data[offset:end]

    @classmethod
    async def get_by_address(
            cls, address: str, offset: int, limit: int
    ) -> list[TronAddressResponse]:
        result = []
        for _ in cls.__data:
            if _.address == address:
                result.append(_)

        end = min(offset + limit, len(cls.__data))
        return result[offset:end]

    @classmethod
    async def create(cls, account: TronAddressResponse) -> TronAddressResponse:
        cls.__data.append(account)
        return account


def get_repository():
    return MockRepository
