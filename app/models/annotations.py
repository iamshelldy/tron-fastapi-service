from datetime import datetime
from typing import Annotated

from sqlalchemy import func
from sqlalchemy.orm import mapped_column


int_pk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime, mapped_column(server_default=func.now())]
