from httpx import AsyncClient, ASGITransport
from pydantic import TypeAdapter
import pytest

from app.main import app
from app.services.tron.repository.mock import get_repository as get_mock_repository
from app.services.tron.schemas import TronAddressResponse
from app.services.tron.service import get_service


@pytest.fixture
def override_dependencies():
    app.dependency_overrides[get_service] = lambda: mock_service()
    yield
    app.dependency_overrides.clear()


def mock_service():
    from app.services.tron.service import TronService
    service = TronService
    service.repo = get_mock_repository()
    return service


@pytest.fixture
async def async_client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


@pytest.mark.asyncio
async def test_get_tron_no_params(override_dependencies, async_client):
    response = await async_client.get("/tron/")
    assert response.status_code == 200

    result = response.json()
    validated = TypeAdapter(list[TronAddressResponse]).validate_python(result)

    assert isinstance(validated, list)
    assert len(validated) == 10
    assert all(isinstance(item, TronAddressResponse) for item in validated)


@pytest.mark.asyncio
async def test_get_tron_pagination_correct_input(override_dependencies, async_client):
    correct_limits_list = [1, 5, 10, 25, 50, 100]
    for limit in correct_limits_list:
        response = await async_client.get(f"/tron/?limit={limit}")
        assert response.status_code == 200

        result = response.json()
        assert len(result) == limit


@pytest.mark.asyncio
async def test_get_tron_pagination_incorrect_input(override_dependencies, async_client):
    incorrect_limits_list = [-1, "asdc", 0, 101, 150]
    for limit in incorrect_limits_list:
        response = await async_client.get(f"/tron/?limit={limit}")
        assert response.status_code == 422


@pytest.mark.asyncio
async def test_post_tron_correct_input(override_dependencies, async_client):
    response = await async_client.post("/tron/", json={"address": "TNMcQVGPzqH9ZfMCSY4PNrukevtDgp24dK"})
    assert response.status_code == 201

    validated = TypeAdapter(TronAddressResponse).validate_python(response.json())
    assert isinstance(validated, TronAddressResponse)


@pytest.mark.asyncio
async def test_post_tron_incorrect_input(override_dependencies, async_client):
    response = await async_client.post("/tron/")
    assert response.status_code == 422

    response = await async_client.post("/tron/", json={"address": "string"})
    assert response.status_code == 422

    response = await async_client.post("/tron/", json={"address": "stringstringstringstringstringstri"})
    assert response.status_code == 400
    assert response.json() == {'detail': 'Incorrect TRON Address'}
