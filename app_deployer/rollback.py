# Import built-in packages
import sys
import logging

# Import modules from this app
from app_deployer.logger import setup_logging
from app_deployer.args import parse_args


def main(argv=None):
    # Get entry_point name
    entry_point = __name__.split('.')[-1]
    # If argv is None, set it to sys.argv
    if argv is None:
        argv = sys.argv
    # Setup logging
    logger = setup_logging(entry_point)
    # Parse command-line arguments
    args = parse_args(argv[1:], entry_point)
    # Set log level
    logger.setLevel(getattr(logging, args.log_level))

    logger.info('This is the {} script...'.format(entry_point))


if __name__ == '__main__':
    sys.exit(main())
