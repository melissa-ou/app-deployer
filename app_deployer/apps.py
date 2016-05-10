# Import from this app


class App:
    """
    An App object containing various properties like a name, git URL, owner, etc.
    """
    def __init__(self, name, git_url, owner, backup_owner, account):
        # Set attributes
        self.name = name
        """Name of the app"""
        self.git_url = git_url
        """Git URL"""
        self.owner = owner
        """App owner"""
        self.backup_owner = backup_owner
        """App backup owner"""
        self.account = account
        """Account the app should be installed to"""


class AppInventory:
    """
    An App Inventory object containing the inventory dictionary, and other properties like lists
    of each of the possible app properties, a function to determine if a given app is in the
    inventory, etc.
    """

    def __init__(self, inventory_dict, inventory_file):
        """
        Returns an AppInventory object

        Parameters
        ----------

        - inventory_dict - *dict* - inventory of apps (read in directly from a YAML app inventory
          file
        - inventory_file - *str* - the YAML file the app inventory was read in from
        """
        # Set attributes
        self.inventory_dict = inventory_dict
        """App inventory dictionary"""
        self.inventory_file = inventory_file
        """App inventory file"""
        # Create separate lists of each app's items
        self.name_list = []
        self.git_url_list = []
        self.owner_list = []
        self.backup_owner_list = []
        self.account_list = []
        for i in range(len(inventory_dict)):
            self.name_list.append(inventory_dict[i]['name'])
            self.git_url_list.append(inventory_dict[i]['git-url'])
            self.owner_list.append(inventory_dict[i]['owner'])
            self.backup_owner_list.append(inventory_dict[i]['backup-owner'])
            self.account_list.append(inventory_dict[i]['account'])

    def __str__(self):
        string = '\n{:90}\n{:^90}\n{:90}\n\n'.format('=' * 90, 'App-Deployer App Inventory',
                                                       '=' * 90)
        for app in self.inventory_dict:
            string += '  {}\n  {}\n\n'.format(app['name'], '-' * len(app['name']))
            string += '    git-url: {}\n'.format(app['git-url'])
            string += '    install-file: {}\n'.format(app['install-file'])
            string += '    owner: {}\n'.format(app['owner'])
            string += '    backup owner: {}\n'.format(app['backup-owner'])
            string += '    account: {}\n'.format(app['account'])
            string += '\n'
        string += 'App inventory file: {}\n\n'.format(self.inventory_file)
        string = string[:-1]  # remove last newline

        return string

    def __repr__(self):
        return self.__str__()

    def is_app(self, name):
        """
        Returns whether a given app name is found in the inventory

        Parameters
        ----------

        - name - *str* - app name to check

        Returns
        -------

        True if the given app is found in the inventory, otherwise False
        """
        return True if name in self.name_list else False
