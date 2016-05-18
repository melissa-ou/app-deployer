# Import from this app


class AppError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class App:
    """
    An App object containing various properties like a name, git URL, owner, etc.
    """
    def __init__(self, name, git_url, owner, install_method, backup_owner=None, account=None):
        # Set attributes
        self.name = name
        """Name of the app"""
        self.git_url = git_url
        """Git URL"""
        self.owner = owner
        """App owner"""
        self.install_method = install_method
        """Install method"""
        self.backup_owner = backup_owner
        """App backup owner"""
        self.account = account
        """Account the app should be installed to"""

    def __str__(self):
        string = ''
        string += 'name: {}\n'.format(self.name)
        string += 'git-url: {}\n'.format(self.git_url)
        string += 'owner: {}\n'.format(self.owner)
        string += 'install method: {}\n'.format(self.install_method)
        string += 'backup owner: {}\n'.format(self.backup_owner)
        string += 'account: {}\n'.format(self.account)

        return string

    def __repr__(self):
        return self.__str__()


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
        self.install_method_list = []
        self.backup_owner_list = []
        self.account_list = []
        for i in range(len(inventory_dict)):
            self.name_list.append(inventory_dict[i].get('name'))
            self.git_url_list.append(inventory_dict[i].get('git-url'))
            self.owner_list.append(inventory_dict[i].get('owner'))
            self.install_method_list.append(inventory_dict[i].get('install-method'))
            self.backup_owner_list.append(inventory_dict[i].get('backup-owner', None))
            self.account_list.append(inventory_dict[i].get('account', None))

    def __str__(self):
        string = '\n{:90}\n{:^90}\n{:90}\n\n'.format('=' * 90, 'App-Deployer App Inventory',
                                                     '=' * 90)
        for app in self.inventory_dict:
            backup_owner = 'None' if 'backup-owner' not in app else app['backup-owner']
            account = 'None' if 'account' not in app else app['account']
            string += '  {}\n  {}\n\n'.format(app['name'], '-' * len(app['name']))
            string += '    git-url: {}\n'.format(app['git-url'])
            string += '    install-method: {}\n'.format(app['install-method'])
            string += '    owner: {}\n'.format(app['owner'])
            string += '    install method: {}\n'.format(app['install-method'])
            string += '    backup owner: {}\n'.format(backup_owner)
            string += '    account: {}\n'.format(account)
            string += '\n'
        string += 'App inventory file: {}\n\n'.format(self.inventory_file)
        string = string[:-1]  # remove last newline

        return string

    def get_dict(self, name):
        """
        Returns a dictionary of all attributes of a given app

        Parameters
        ----------

        - name - *str* - name of app

        Returns
        -------

        *dict* - dictionary of all attributes of the app
        """
        # Make sure this name matches an app in the inventory
        if not self.is_app(name):
            raise AppError('Cannot find an app matching the name {}'.format(name))
        # Find the dictionary where the key 'name' matches the given name
        app_dict = next(item for item in self.inventory_dict if item['name'] == name)

        return app_dict

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

    def get_app(self, name):
        """
        Returns an App instance created from the app with the given name

        Parameters
        ----------

        - name - *str* - app name

        Returns
        -------

        App instance
        """
        # Make sure this name matches an app in the inventory
        if not self.is_app(name):
            raise AppError('Cannot find an app matching the name {}'.format(name))
        # Get all attributes of the app in a dictionary
        app_dict = self.get_dict(name)
        # Create an instance of the app
        app = App(name, app_dict['git-url'], app_dict['owner'], app_dict['install-method'],
                  backup_owner=app_dict.get('backup-owner', None),
                  account=app_dict.get('account', None))

        return app
