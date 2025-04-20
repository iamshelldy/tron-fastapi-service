import logging

from fastapi import Depends
from httpx import HTTPStatusError
from tronpy.exceptions import BadAddress

from app.core.config import config
from app.services.tron.errors import BadTronAddressError, InternalServerError
from app.services.tron.repository.base import AbstractRepository
from app.services.tron.repository.mock import get_repository
from app.services.tron.schemas import TronAddressGetRequest, TronAddressPostRequest
from app.services.tron.utils import get_address_info


logger = logging.getLogger("app")


class TronService:
    repo: AbstractRepository

    @classmethod
    async def get(cls, request: TronAddressGetRequest):
        offset = (request.page - 1) * request.limit

        if request.address:
            return await cls.repo.get_by_address(request.address, offset, request.limit)
        else:
            return await cls.repo.get_all(offset, request.limit)

    @classmethod
    async def post(cls, request: TronAddressPostRequest):
        try:
            data = await get_address_info(
                request.address, api_key=config.TRON_API_KEY.get_secret_value()
            )
            return await cls.repo.create(data)

        except BadAddress:
            logger.warning(f"Address {request.address} is not valid")
            raise BadTronAddressError

        except HTTPStatusError as e:
            if 401 == e.response.status_code:
                logger.error("API key is not valid")

        except Exception as e:
            logger.error(e)

        raise InternalServerError


def get_service(repo: AbstractRepository = Depends(get_repository)):
    service = TronService
    service.repo = repo
    return service
