# Import from this app
from app_deployer import app_inventory


class App:
    def __init__(self, name, git_url, owner, backup_owner, account):
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
