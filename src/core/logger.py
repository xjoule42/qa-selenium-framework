import logging
from logging.handlers import RotatingFileHandler

from config.settings import LOGS_DIR


class Logger:
    """Factory class for creating configured application loggers."""

    @classmethod
    def get_logger(cls, name: str) -> logging.Logger:
        """
        Return a configured logger instance.

        Args:
            name: Logger name.

        Returns:
            Configured logger.
        """

        logger = logging.getLogger(name)

        # Avoid adding handlers multiple times.
        if logger.handlers:
            return logger

        logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
        )

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        # File handler
        file_handler = RotatingFileHandler(
            LOGS_DIR / "framework.log",
            maxBytes=5 * 1024 * 1024,  # 5 MB
            backupCount=3,
            encoding="utf-8",
        )
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

        # Prevent duplicate messages from the root logger.
        logger.propagate = False

        return logger