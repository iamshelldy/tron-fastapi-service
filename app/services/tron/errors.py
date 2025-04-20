class BaseTronServiceError(Exception):
    status_code: int
    message: str


class InternalServerError(BaseTronServiceError):
    status_code = 500
    message = "Internal Server Error"


class BadTronAddressError(BaseTronServiceError):
    status_code = 400
    message = "Incorrect TRON Address"

