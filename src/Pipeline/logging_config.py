import logging
from typing import Optional

def get_logger(name: Optional[str] = None) -> logging.Logger:
    logger = logging.getLogger(name or "pipeline")
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        h = logging.StreamHandler()
        fmt = logging.Formatter(
            fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        h.setFormatter(fmt)
        logger.addHandler(h)
    return logger
