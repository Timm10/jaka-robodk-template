import logging
from config_helper import load_config

config = load_config()
LOG_TO_FILE = config.get("log_to_file", False)

logger = logging.getLogger("JakaLogger")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s")

if LOG_TO_FILE:
    fh = logging.FileHandler("jaka_log.txt")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
logger.addHandler(ch)
