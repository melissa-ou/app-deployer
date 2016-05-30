# Import built-in packages
import logging


# Get the logger
logger = logging.getLogger(__name__)


class DeploymentError(Exception):
    """
    Custom DeploymentError Exception
    """
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class Deployment:
    """
    A class containing methods for actually deploying the app
    """

    def __init__(self, app, host, install_method, local_templ_dir='.', local_work_dir='.'):
        """
        Returns Deployment object

        Parameters
        ----------

        - app - *App* - App instance to deploy
        - host - *Host* - Host instance to deploy to
        - install_method - *str* - method for installing the app
        - local_templ_dir - *str* - local (on Ansible host machine) dir containing templates
          (optional)
        - local_work_dir = *str* - local (on Ansible host machine) temp working dir for templates,
          etc. (optional)
        """
        # Set attributes
        self.app = app
        """App to deploy"""
        self.host = host
        """Host to deploy to"""
        self.install_method = install_method
        """Install method"""
        self.local_templ_dir = local_templ_dir
        """Local templates directory"""
        self.local_work_dir = local_work_dir
        """Local working directory"""

    def __str__(self):
        string = ''
        string += 'app: {}\n'.format(self.app.name)
        string += 'host: {}\n'.format(self.host)
        string += 'install method: {}\n'.format(self.install_method)
        string += 'work dir: {}\n'.format(self.work_dir)

        return string

    def execute(self):
        """
        Executes the deployment
        """
        if self.install_method == 'ansible':
            logger.info('Deploying {} to {} using {}...'.format(self.app.name, self.host,
                                                                self.install_method))
        elif self.install_method == 'make':
            logger.info('Deploying {} to {} using {}...'.format(self.app.name, self.host,
                                                                self.install_method))
        else:
            return DeploymentError(
                'The install method for the app {} is set to {}, which is not a valid option - it '
                'must be set to either \'ansible\' or \'make\''.format(self.app.name,
                                                                       self.install_method)
            )
