import logging
from pydub.generators import Sine
from pydub.playback import play
import time

class AudioFormatter(logging.Formatter):

    def __init__(self, generator=Sine(440)):
        super().__init__()
        self._generator = generator

    def format(self, record):
        # TODO remove class specific knowledge
        aseg = self._generator.to_audio_segment(duration=100)
        play(aseg)
        # TODO add formatting options from parent
        return(super().format(record))

def create_test_logger():
    logger = logging.getLogger("test_logger")
    handler = logging.StreamHandler()
    handler.setFormatter(AudioFormatter())
    logger.addHandler(handler)
    return logger