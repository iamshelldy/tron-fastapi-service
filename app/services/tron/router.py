from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from app.services.tron.errors import BaseTronServiceError
from app.services.tron.schemas import (TronAddressGetRequest, TronAddressPostRequest,
                                       TronAddressResponse)
from app.services.tron.service import TronService, get_service

router = APIRouter(prefix="/tron", tags=["Work with TRON addresses"])


@router.get("/")
async def get_tron_info(
        params: TronAddressGetRequest = Depends(),
        service: TronService = Depends(get_service),
) -> list[TronAddressResponse]:
    try:
        return await service.get(params)
    except BaseTronServiceError as e:
        raise HTTPException(
            status_code=e.status_code,
            detail=e.message,
        )



@router.post("/", status_code=status.HTTP_201_CREATED)
async def post_tron_info(
        params: TronAddressPostRequest,
        service: TronService = Depends(get_service),
) -> TronAddressResponse:
    try:
        return await service.post(params)
    except BaseTronServiceError as e:
        raise HTTPException(
            status_code=e.status_code,
            detail=e.message,
        )
