import logging
from venv import create
from visualog import AudioFormatter, create_test_logger
import random
import time

logger = create_test_logger()
logger.setLevel(logging.DEBUG)

probabilities = {
    logging.CRITICAL: 0.01,
    logging.ERROR: 0.05,
    logging.WARNING: 0.1,
    logging.INFO: 0.2,
    logging.DEBUG: 0.5,
}



while True:
    draw = random.random()
    for level, probability in probabilities.items():
        if draw < probability:
            logger.log(level, "test")

    time.sleep(0.1)