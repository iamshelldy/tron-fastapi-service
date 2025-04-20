from fastapi import APIRouter, Depends

from app.services.tron.schemas import (TronAddressGetRequest, TronAddressPostRequest,
                                       TronAddressResponse)

router = APIRouter(prefix="/tron", tags=["Work with TRON addresses"])


@router.get("/")
async def get_tron_info(
        params: TronAddressGetRequest = Depends()
) -> list[TronAddressResponse]:
    # Here will be service call
    pass



@router.post("/")
async def post_tron_info(
        params: TronAddressPostRequest
) -> TronAddressResponse:
    # Here will be service call
    pass
