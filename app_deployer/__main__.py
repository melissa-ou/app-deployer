# Import built-in packages
import sys
import logging
import argparse

# Import CPC packages
from app_deployer import config


# Parse command-line arguments
def parse_args(argv):
    """
    Parse the command line args

    Note that the argv argument will be parsed instead of sys.argv because
    the test suite will need to execute the main() function, and will
    therefore need to pass the given arguments to that function, as opposed
    to the main() function getting them from sys.argv.

    Parameters
    ----------

    - argv - *list of strings* - argument list containing the elements from
    sys.argv, except the first element (sys.argv[0]) which is the script name
    """
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(add_help=False, usage='%(prog)s [options] <app> <host>')

    # Add positional arguments
    parser.add_argument(
        'app_name', metavar='app', type=str, nargs='+', help='app to deploy')
    parser.add_argument(
        'host', metavar='host', type=str, nargs='+', help='host to deploy to')

    # Add a required argument group
    group = parser.add_argument_group('required arguments')

    # Add required arguments


    # Add an optional argument group
    group = parser.add_argument_group('optional arguments')
    group.add_argument(
        '-h', '--help', dest='help', action='help',
        help='show this help message and exit')
    group.add_argument(
        '--log-level', dest='log_level',
        help='logging level - choices: DEBUG, INFO, WARNING, ERROR, CRITICAL',
        metavar='<LEVEL>', default='INFO',
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL",
                 "debug", "info", "warning", "error", "critical"])

    # If no options are set, print help and exit, otherwise parse args
    if len(argv) < 2:
        parser.print_help()
        sys.exit()
    else:
        args = parser.parse_args(argv)
    # If the help option was set, print help and exit
    if hasattr(args, 'help'):
        parser.print_help()
        sys.exit()
    # Uppercase log level
    args.log_level = args.log_level.upper()

    return args


def main(argv=None):
    # If argv is None, set it to sys.argv
    if argv is None:
        argv = sys.argv
    # Setup logging
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(asctime)s - %(name)s - %(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %I:%M:%S%p'
    )
    logger = logging.getLogger('app-deployer')

    # --------------------------------------------------------------------------
    # Parse command-line arguments
    #
    args = parse_args(argv[1:])
    # Set log level
    logger.setLevel(getattr(logging, args.log_level))

    logger.info("This is the main function.")


if __name__ == "__main__":
    sys.exit(main())
