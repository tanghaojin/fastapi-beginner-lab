import logging

logger = logging.getLogger(__name__)


def log_notification(message: str) -> None:
    logger.info("notification queued: %s", message)
