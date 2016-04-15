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
        default_config = yaml.load(resource_string('app_deployer', 'config.yml'))
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
        user_config = default_config
    except Exception:
        print('There was a problem reading {}'.format(config_file))
        sys.exit(1)
    # If the user config file is empty, set the config data equal to the default data
    if not user_config:
        user_config = default_config
    # Override default values with the user-defined values
    try:
        config = {**default_config, **user_config}
    except Exception:
        config = default_config
    # Return the config dict
    return config

config = load_config()
