from sqlalchemy import Column, BigInteger
from sqlalchemy.orm import Mapped

from app.models.base import Base


class Account(Base):
    address: Mapped[str]
    balance: Mapped[float]
    bandwidth: Mapped[int] = Column(BigInteger, nullable=False)
    energy: Mapped[int] = Column(BigInteger, nullable=False)
