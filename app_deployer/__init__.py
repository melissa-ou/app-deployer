# -*- coding: utf-8 -*-

# Import built-in packages
import os
import sys
from pkg_resources import resource_string

# Import third-party packages
import yaml
import appdirs


__author__ = 'Mike Charles'
__email__ = 'mike.charles@noaa.gov'
__version__ = 'v0.1.0'


app_inventory_file = None


def merge_dicts(source, destination):
    for key, value in source.items():
        if isinstance(value, dict):
            # get node or create one
            node = destination.setdefault(key, {})
            merge_dicts(value, node)
        else:
            destination[key] = value
    return destination


# Load config data
def load_config():
    """
    Loads config values from the default config.yml file installed with the package,
    and overrides those values with values found in a config.yml file in ~/.config/<app-name>
    """
    # ----------------------------------------------------------------------------------------------
    # Load default config
    #
    try:
        config = yaml.load(resource_string('app_deployer', 'config.yml'))
    except Exception:
        print('Couldn\'t load default configuration data. Something went wrong with the '
              'installation.')
        sys.exit(1)
    # ----------------------------------------------------------------------------------------------
    # Load an optional config file with user-defined values that will override default values
    #
    # Try to read the config.yml file in <USER_CONFIG_DIR>/<app-name> - note that
    # <USER_CONFIG_DIR> depends on the OS. For example, in Mac OS it's
    # /Users/<username>/Library/Application Support, in Linux it's ~/.config.
    config_dir = appdirs.user_config_dir("app-deployer")
    config_file = os.path.expanduser('{}/config.yml'.format(config_dir))
    try:
        with open(config_file) as f:
            user_config = yaml.load(f)
    except FileNotFoundError:
        user_config = config
    except Exception:
        print('There was a problem reading {}'.format(config_file))
        sys.exit(1)
    # If the user config file is empty, set the config data equal to the default data
    if not user_config:
        user_config = config
    # Override default values with the user-defined values
    try:
        config = merge_dicts(user_config, config)
    except Exception:
        config = config
    # Return the config dict
    return config


def load_app_inventory(type, file=None):
    """
    Loads an inventory of apps deployable by App-Deployer

    Supports reading an inventory of apps from a YAML file or a MySQL table

    Parameters
    ----------

    - type - str - type of inventory ('file' [default] or 'mysql')
    - file - str - inventory file name - only needed when type=='file'
    """
    global app_inventory_file  # Will set this to the file that is successfully loaded
    app_inventory = None
    # File-based inventory
    if type == 'file':
        # Highest priority is a file specified in the config file
        if file:
            with open(file) as f:
                app_inventory = yaml.load(f)
                app_inventory_file = file
        # Otherwise try the lower-priority files
        else:
            # Establish a list of inventory dirs
            inventory_dirs = [
                appdirs.user_config_dir("app-deployer"),  # User config dir
                os.path.abspath(os.getcwd())  # current working dir
            ]
            # Loop over inventory dirs
            for inventory_dir in inventory_dirs:
                # Append default file name to inventory dir
                file = '{}/{}'.format(inventory_dir, 'app-inventory.yml')
                # Try to load the YAML file
                try:
                    with open(file) as f:
                        app_inventory = yaml.load(f)
                        app_inventory_file = file
                        break
                except:
                    pass
    if not app_inventory:
        raise ValueError('Could not load an app inventory...')
    return app_inventory


# Load config
config = load_config()

# Load app inventory and save in where module
if 'file' in config['app-inventory']:
    file = config['app-inventory']['file']
else:
    file = None
app_inventory = load_app_inventory(config['app-inventory']['type'], file)

# Save the name of the file that the app inventory was loaded from
if config['app-inventory']['type'] == 'file':
    config['app-inventory']['file'] = app_inventory_file
