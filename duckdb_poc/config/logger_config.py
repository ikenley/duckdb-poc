import logging
import logging.config
import os


def setup_logger(log_level=logging.INFO, log_file="duckdb_poc.log"):
    # Create logs directory if it doesn't exist
    os.makedirs("logs", exist_ok=True)

    # Configure logging
    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {"format": "%(asctime)s-%(name)s-%(levelname)s-%(message)s"},
            "detailed": {
                "format": "%(asctime)s-%(name)s-%(levelname)s-%(message)s - [%(filename)s:%(lineno)d]"
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "default",
                "level": log_level,
            },
            "file": {
                "class": "logging.FileHandler",
                "formatter": "detailed",
                "filename": f"logs/{log_file}",
                "level": log_level,
            },
        },
        "root": {
            "handlers": ["console", "file"],
            "level": log_level,
        },
    }

    logging.config.dictConfig(logging_config)
    logger = logging.getLogger()
    logger.info("Logger initialized.")
    return logger
