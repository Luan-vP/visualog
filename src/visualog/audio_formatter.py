import logging
from pydub.generators import Sine
from pydub.playback import play
import time

class AudioFormatter(logging.Formatter):
    frequencies = {
        logging.CRITICAL: 1440,
        logging.ERROR: 720,
        logging.WARNING: 360,
        logging.INFO: 180,
        logging.DEBUG: 90,
    }

    volumes_db = {
        logging.CRITICAL: 0,
        logging.ERROR: -1,
        logging.WARNING: -3,
        logging.INFO: -4,
        logging.DEBUG: -6,
    } 


    def __init__(self, generator_cls=Sine):
        super().__init__()
        self._generators = {level: generator_cls(frequency) for level, frequency in self.frequencies.items()}

    def format(self, record):
        # TODO remove class specific knowledge
        print(self.volumes_db[record.levelno])
        aseg = self._generators[record.levelno].to_audio_segment(duration=100, volume=self.volumes_db[record.levelno])
        play(aseg)
        # TODO add formatting options from parent
        return(super().format(record))

def create_test_logger():
    logger = logging.getLogger("test_logger")
    handler = logging.StreamHandler()
    handler.setFormatter(AudioFormatter())
    logger.addHandler(handler)
    return logger