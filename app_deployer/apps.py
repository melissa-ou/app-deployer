# Import from this app


class App:
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
    def __init__(self, inventory_dict, inventory_file):
        # Set attributes
        self.inventory_dict = inventory_dict
        """App inventory dictionary"""
        self.inventory_file = inventory_file
        """App inventory file"""
        # Create separate lists of each app's items
        name_list = []
        git_url_list = []
        owner_list = []
        backup_owner_list = []
        account_list = []
        for i in range(len(inventory_dict)):
            name_list.append(inventory_dict[i]['name'])
            git_url_list.append(inventory_dict[i]['git-url'])
            owner_list.append(inventory_dict[i]['owner'])
            backup_owner_list.append(inventory_dict[i]['backup-owner'])
            account_list.append(inventory_dict[i]['account'])

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

