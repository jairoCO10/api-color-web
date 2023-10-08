import logging
from logging.handlers import TimedRotatingFileHandler

class CustomLogger:
    def __init__(self, filename):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        log_formatter = logging.Formatter('%(asctime)s [%(levelname)s] - %(message)s')
        log_handler = TimedRotatingFileHandler(
            filename=filename,
            when='W0',
            interval=1,
        )
        log_handler.setFormatter(log_formatter)
        self.logger.addHandler(log_handler)

    def log(self, data):
        self.logger.info(data)
