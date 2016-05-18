# Import built-in packages
import sys
import logging

# Import third-party packages
import appdirs

# Import modules from this app
from app_deployer.logger import setup_logging
from app_deployer.args import parse_args
from app_deployer.deployment import DeploymentError, Deployment

# Import variables from this app
from app_deployer import app_inventory, ansible_exe, host_inventory


def main(argv=None):
    # ----------------------------------------------------------------------------------------------
    # Setup
    #
    # Get entry_point name
    entry_point = __name__.split('.')[-1].split('_')[0]
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
    deployment = Deployment(app, args.host, app.install_method)
    deployment.execute()


if __name__ == '__main__':
    sys.exit(main())
