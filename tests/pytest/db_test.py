from datetime import datetime

import pytest
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.main import app
from app.models.base import Base
from app.services.tron.repository.db import get_repository
from app.services.tron.schemas import TronAddressResponse, TronAddressGetRequest


TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"
engine = create_async_engine(TEST_DATABASE_URL)
AsyncSession = async_sessionmaker(engine, expire_on_commit=False)


@pytest.fixture(scope="function", autouse=True)
async def prepare_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@pytest.fixture
def override_dependencies():
    app.dependency_overrides[get_repository] = lambda: mock_repository()
    yield
    app.dependency_overrides.clear()


def mock_repository():
    from app.services.tron.repository.db import DBRepository
    repo = DBRepository
    repo.session = AsyncSession
    return repo


@pytest.mark.asyncio
async def test_db(override_dependencies):
    repo = mock_repository()

    test_post_data = TronAddressResponse(
        address="stringstringstringstringstringstri",
        created_at=datetime.now(),
        balance=1105.0,
        bandwidth=1325,
        energy=235,
    )
    # Write data to DB.
    await repo.create(test_post_data)

    test_get_data = TronAddressGetRequest(address="stringstringstringstringstringstri", page=1, limit=1)
    offset = (test_get_data.page - 1) * test_get_data.limit
    # Read data from DB.
    result = await repo.get_by_address(test_get_data.address, offset, test_get_data.limit)

    validated = TronAddressResponse.model_validate(result[0])
    assert validated == test_post_data

