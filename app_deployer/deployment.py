# Import built-in packages
import os
import sys
import subprocess

# Import third-party packages
import appdirs

# Import from this app
from app_deployer import config


def get_ansible_exe():
    # Get directory from config file
    if config['ansible'] is not None:
        ansible_bin_dir = config['ansible']['path']
    # Otherwise default to this entry_point's parent directory
    else:
        ansible_bin_dir = os.path.dirname(sys.argv[0])
    # See if there's an ansible script in this dir
    try:
        subprocess.check_output(
            '{}/ansible --version'.format(ansible_bin_dir),
            stdin=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True)
        return '{}/ansible'.format(ansible_bin_dir)
    except subprocess.CalledProcessError:
        return None
