# Import built-in packages
import logging
import sys


class CustomFormatter(logging.Formatter):
    # default_fmt = logging.Formatter('[%(asctime)s - %(name)s - %(levelname)s] %(message)s')
    default_fmt = logging.Formatter('%(message)s')
    info_fmt = logging.Formatter('%(message)s')

    def __init__(self, fmt='%(message)s', datefmt='%Y-%m-%d %I:%M:%S%p'):
        logging.Formatter.__init__(self, fmt, datefmt)

    def format(self, record):
        if record.levelno == logging.INFO:
            return self.info_fmt.format(record)
        else:
            return self.default_fmt.format(record)


def setup_logging(name):
    fmt = CustomFormatter(datefmt='%Y-%m-%d %I:%M:%S%p')
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(fmt)
    logging.root.addHandler(handler)
    logging.root.setLevel(logging.INFO)

    return logging.getLogger(name)
