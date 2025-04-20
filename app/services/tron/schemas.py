from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict


class TronAddressPostRequest(BaseModel):
    address: str = Field(min_length=34, max_length=34, description="TRON address (optional)")


class TronAddressGetRequest(BaseModel):
    address: str | None = Field(default=None, min_length=34, max_length=34, description="TRON address")
    page: int = Field(default=1, ge=1, description="Page number")
    limit: int = Field(default=10, ge=1, le=100, description="Number of results")


# Don't use inheritance to clearly define the order of fields.
class TronAddressResponse(BaseModel):
    address: str = Field(description="TRON address")
    created_at: datetime = Field(description="Data timestamp")
    balance: float = Field(description="Address balance")
    bandwidth: int = Field(description="Address bandwidth")
    energy: int = Field(description="Address energy")
