# Import built-in packages
import subprocess


class Host:
    """
    A Host object containing various properties like a name, OS, app_root, etc.
    """

    def __init__(self, name, os, app_root):
        # Set attributes
        self.name = name
        """Name of the app"""
        self.os = os
        """Operating system"""
        self.app_root = app_root
        """App root directory"""


class HostInventory:
    """
    A Host Inventory object containing the inventory list, a function to determine if a given
    host name is in the inventory, etc.
    """

    def __init__(self, ansible_exe, app_root):
        """
        Returns an AppInventory object

        Parameters
        ----------

        - ansible_exe - *str* - Ansible executable
        - app_root - *str* - App root directory where all apps should be deployed into
        """
        # Set attributes
        self.ansible_exe = ansible_exe
        """Ansible executable"""
        self.app_root = app_root
        """App inventory dictionary"""
        self.host_list = subprocess.getoutput(
            '{} --list-hosts all | tail +2'.format(ansible_exe)).split()

    def __str__(self):
        string = '\n{:90}\n{:^90}\n{:90}\n\n'.format('=' * 90, 'App-Deployer Host Inventory',
                                                     '=' * 90)
        for host in self.host_list:
            string += '  - {}\n'.format(host)

        return string

    def __repr__(self):
        return self.__str__()

    def is_host(self, name):
        """
        Returns whether a given app name is found in the inventory

        Parameters
        ----------

        - name - *str* - app name to check

        Returns
        -------

        True if the given host is found in the inventory, otherwise False
        """
        return True if name in self.host_list else False
