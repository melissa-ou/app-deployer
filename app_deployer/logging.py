# Import built-in packages
import logging


def setup_logging(name):
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(asctime)s - %(name)s - %(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %I:%M:%S%p'
    )
    return logging.getLogger(name)
