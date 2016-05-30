# Import built-in packages
import os
import sys
import shutil
import logging
import argparse
from tempfile import mkdtemp

# Import third-party packages
import appdirs
import coloredlogs

# Import modules from this app
from app_deployer.deployment import DeploymentError, Deployment

# Import variables from this app
from app_deployer import app_inventory, ansible_exe, host_inventory


def parse_args(argv):
    """
    Parse the command line args

    Note that the argv argument will be parsed instead of sys.argv because the test suite will
    need to execute the main() function, and will therefore need to pass the given arguments to
    that function, as opposed to the main() function getting them from sys.argv.

    Parameters
    ----------

    - argv - *list of str* - argument list containing the elements from sys.argv, except the
    first element (sys.argv[0]) which is the script name

    Returns
    -------

    - *ArgumentParser object* - parsed arguments
    """
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(add_help=False, usage='%(prog)s [options] <app> <host>')

    # Add positional arguments
    parser.add_argument('app_name', metavar='app', type=str, nargs='?', help='app to deploy')
    parser.add_argument('host', metavar='host', type=str, nargs='?', help='host to deploy to')

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
        help='list apps that can be deployed or rolled back - won\'t actually deploy or rollback '
             'anything')
    group.add_argument(
        '--list-hosts', dest='list_hosts', action='store_true',
        help='list hosts that apps can be deployed to or rolled back on - won\'t actually deploy '
             'or rollback anything')

    # If less than 2 positional args are set, and no read-only args have been provided, print help
    # and exit, otherwise parse args (read-only args include things like --list-apps, which just
    # lists deployable apps and then exits)
    read_only_args = ['--list-apps', '--list-hosts']
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


def main(argv=None):
    # ----------------------------------------------------------------------------------------------
    # Setup
    #
    # Get script dir
    script_dir = os.path.dirname(os.path.realpath(__file__))
    # Create a temporary work directory
    work_dir = mkdtemp(prefix='app-deployer-')
    # Get entry_point name
    entry_point = __name__.split('.')[-1].split('_')[0]
    # If argv is None, set it to sys.argv
    if argv is None:
        argv = sys.argv
    # Parse command-line arguments
    args = parse_args(argv[1:])
    # Setup logging
    logging.basicConfig(level=args.log_level)  # set log level for root logger
    logger = logging.getLogger('app_deployer')  # get instance of logger
    coloredlogs.install(fmt='%(message)s')  # colorize logging output

    # ----------------------------------------------------------------------------------------------
    # Print out app inventory
    #
    if args.list_apps:
        logger.info(app_inventory)
        sys.exit()

    # ----------------------------------------------------------------------------------------------
    # Print out hosts inventory
    #
    if args.list_hosts:
        logger.info(host_inventory)
        sys.exit()

    # ----------------------------------------------------------------------------------------------
    # Make sure ansible is installed and can be executed
    #
    if ansible_exe is None:
        config_dir = appdirs.user_config_dir('app-deployer')
        logger.fatal('ansible not found - please set ansible.path in {}/config.yml'.format(
            config_dir))
        sys.exit(1)

    # ----------------------------------------------------------------------------------------------
    # Validate the positional args
    #
    # App
    if not app_inventory.is_app(args.app_name):
        logger.fatal('Can\'t {} {} - not found in the app inventory. Run {} --list-apps to print '
                     'out the app inventory'.format(entry_point, args.app_name, entry_point))
        sys.exit(1)
    # Host
    if not host_inventory.is_host(args.host):
        logger.fatal('{} is not a valid host - make sure it\'s defined in your inventory file - '
                     'see Ansible documentation online'.format(args.host))
        sys.exit(1)

    # ----------------------------------------------------------------------------------------------
    # Create an App instance
    #
    app = app_inventory.get_app(args.app_name)

    # ----------------------------------------------------------------------------------------------
    # Deploy the app
    #
    deployment = Deployment(app, args.host, app.install_method,
                            local_templ_dir='{}/../ansible-templates'.format(script_dir),
                            local_work_dir=work_dir)
    deployment.execute()

    # ----------------------------------------------------------------------------------------------
    # Cleanup
    #
    # Remove work dir
    os.chdir(os.path.expanduser('~'))
    shutil.rmtree(work_dir)


if __name__ == '__main__':
    sys.exit(main())
