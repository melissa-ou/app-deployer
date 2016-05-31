# Import built-in packages
import logging

# Import packages from this app
from .templates import render_templates


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

    def __init__(self, app, host, install_method, local_template_dir='.', local_work_dir='.'):
        """
        Returns Deployment object

        Parameters
        ----------

        - app - *App* - App instance to deploy
        - host - *Host* - Host instance to deploy to
        - install_method - *str* - method for installing the app
        - local_template_dir - *str* - local (on Ansible host machine) dir containing templates
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
        self.local_template_dir = local_template_dir
        """Local templates directory"""
        self.local_work_dir = local_work_dir
        """Local working directory"""

    def __str__(self):
        string = ''
        string += 'app: {}\n'.format(self.app.name)
        string += 'host: {}\n'.format(self.host)
        string += 'install method: {}\n'.format(self.install_method)
        string += 'local template dir: {}\n'.format(self.local_template_dir)
        string += 'local work dir: {}\n'.format(self.local_work_dir)

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
            templ_vars = {
                'app-name': self.app.name
            }
            # Render the templates
            render_templates('{}/{}'.format(self.local_template_dir, self.install_method),
                             '{}/ansible-templates'.format(self.local_work_dir),
                             templ_vars=templ_vars)
        else:
            return DeploymentError(
                'The install method for the app {} is set to {}, which is not a valid option - it '
                'must be set to either \'ansible\' or \'make\''.format(self.app.name,
                                                                       self.install_method)
            )
