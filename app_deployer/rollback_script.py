# Import built-in packages
import sys
import logging

# Import modules from this app
from app_deployer.logger import setup_logging
from app_deployer.args import parse_args
import app_deployer.hosts as hosts
from app_deployer import app_inventory
from app_deployer.apps import App


def main(argv=None):
    # ----------------------------------------------------------------------------------------------
    # Setup
    #
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

    # ----------------------------------------------------------------------------------------------
    # Print out app inventory
    #
    if args.list_apps:
        logger.info(app_inventory)
        sys.exit()


if __name__ == '__main__':
    sys.exit(main())
