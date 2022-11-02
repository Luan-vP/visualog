import logging
from venv import create
from visualog import AudioFormatter, set_loopback_device, create_test_logger
from random import randint
import time

set_loopback_device()

logger = create_test_logger()



while True:
    logger.error('test')
    time.sleep(randint(1, 2))