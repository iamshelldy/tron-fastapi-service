import inflect
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import Mapped, DeclarativeBase, declared_attr

from app.models.annotations import int_pk, created_at


p = inflect.engine()


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    id: Mapped[int_pk]
    created_at: Mapped[created_at]

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return p.plural(cls.__name__.lower())
