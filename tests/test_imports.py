import pytest
import logging
from pydub.generators import Sine
from visualog import AudioFormatter
from unittest import mock

def test_can_create_AudioFormatter():

    handler = logging.StreamHandler()
    handler.setFormatter(AudioFormatter())
    logger = logging.getLogger("visualog_test_logger")

    logger.addHandler(handler)
    logging.info('test')

    # OK no errors, but how to test that the audio is playing?




