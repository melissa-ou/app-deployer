# Import from this app
from app_deployer import app_inventory, app_inventory_file


def list_apps(entry_point):
    """
    Lists the deployable apps from the app inventory
    """
    if entry_point == 'deploy':
        action = 'deployed'
        line = '=' * 25
    else:
        action = 'rolled back'
        line = '=' * 28
    app_list = '\n{:90}\n{:^90}\n{:90}\n\n'.format('=' * 90, 'App-Deployer App Inventory', '=' * 90)
    app_list += 'App inventory file: {}\n\n'.format(app_inventory_file)
    app_list += 'Apps that can be {}\n'.format(action)
    app_list += '{}\n\n'.format(line)
    for app in app_inventory:
        app_list += '  {}\n  {}\n\n'.format(app['name'], '-' * len(app['name']))
        app_list += '    git-url: {}\n'.format(app['git-url'])
        app_list += '    install-file: {}\n\n'.format(app['install-file'])
    app_list = app_list[:-1]  # remove last newline
    return app_list
