import logging.config

# Load the logging configuration
logging.config.fileConfig('logging_config.ini')

# Create loggers
logger = logging.getLogger("sampleLogger")


def main():
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")


if __name__ == "__main__":
    main()
