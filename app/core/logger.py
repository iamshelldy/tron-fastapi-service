import logging


def init_logger() -> None:
    formatter = logging.Formatter("%(levelname)s: %(message)s")

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger("app")
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
