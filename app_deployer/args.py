# Import built-in packages
import sys
import argparse


def parse_args(argv, entry_point):
    """
    Parse the command line args

    Note that the argv argument will be parsed instead of sys.argv because the test suite will
    need to execute the main() function, and will therefore need to pass the given arguments to
    that function, as opposed to the main() function getting them from sys.argv.

    Parameters
    ----------

    - argv - *list of str* - argument list containing the elements from sys.argv, except the
    first element (sys.argv[0]) which is the script name
    - entry_point - *str* - name of the entry_point (in setup.py) to parse args for
    """
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(add_help=False, usage='%(prog)s [options] <app> <host>')

    # Add positional arguments
    parser.add_argument(
        'app_name', metavar='app', type=str, nargs='?', help='app to deploy')
    parser.add_argument(
        'host', metavar='host', type=str, nargs='?', help='host to deploy to')

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
    group.add_argument(
        '--list-apps', dest='list_apps', action='store_true',
        help='list deployable apps - won\'t deploy or rollback anything')

    # If less than 2 positional args are set, and no read-only args have been provided, print help
    # and exit, otherwise parse args (read-only args include things like --list-apps, which just
    # lists deployable apps and then exits)
    read_only_args = ['--list-apps']
    if len(argv) < 2 and not list(set(argv) & set(read_only_args)):
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
