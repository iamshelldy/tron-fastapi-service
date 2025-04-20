from datetime import datetime

from tronpy import AsyncTron
from tronpy.providers import AsyncHTTPProvider

from app.services.tron.schemas import TronAddressResponse


async def get_address_info(address: str, api_key: str) -> TronAddressResponse:
    async with AsyncTron(AsyncHTTPProvider(api_key=api_key)) as client:
        account: dict = await client.get_account(address)
        # Get TRX balance.
        balance = account.get("balance", 0) / 1_000_000
        # Get energy information.
        resources: dict = await client.get_account_resource(address)
        energy_limit = resources.get("EnergyLimit", 0)
        energy_used = resources.get("EnergyUsed", 0)
        energy = energy_limit - energy_used
        # Get bandwidth information.
        bandwidth: int = await client.get_bandwidth(address)
        return TronAddressResponse(
            address=address,
            created_at=datetime.now(),
            balance=balance,
            bandwidth=bandwidth,
            energy=energy,
        )
