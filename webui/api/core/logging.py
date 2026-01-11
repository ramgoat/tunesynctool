from logging import getLogger, StreamHandler, FileHandler, Formatter, INFO, DEBUG, WARNING, ERROR, CRITICAL
import sys
import os

logger = getLogger("tunesynctool-api")

formatter = Formatter("%(asctime)s - %(levelname)s - %(message)s")


stream_handler = StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)

file_handler = FileHandler("app.log")
file_handler.setFormatter(formatter)

logger.handlers = [stream_handler, file_handler]

# Get log level from environment variable, default to INFO
log_level_str = os.getenv("LOG_LEVEL", "INFO").upper()
log_level_map = {
    "DEBUG": DEBUG,
    "INFO": INFO,
    "WARNING": WARNING,
    "ERROR": ERROR,
    "CRITICAL": CRITICAL,
}
log_level = log_level_map.get(log_level_str, INFO)
logger.setLevel(log_level)