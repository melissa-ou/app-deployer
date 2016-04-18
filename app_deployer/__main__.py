# Import built-in packages
import sys
import logging

# Import CPC packages
from app_deployer import config


def main(argv=None):
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(asctime)s - %(name)s - %(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %I:%M:%S%p'
    )
    logger = logging.getLogger('app-deployer')
    logger.info("This is the main function.")


if __name__ == "__main__":
    main(sys.argv[1:])
