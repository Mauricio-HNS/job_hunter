# Job_Hunter/utils/logger.py
import logging

def setup_logger():
    logger = logging.getLogger("Job_Hunter")
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        ch = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    return logger
