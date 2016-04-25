import unittest

# Try to import app_deployer, which will execute the functions in __init__.py
import app_deployer


def test_config_var_not_empty():
    """Ensure the config variable isn't empty"""
    assert app_deployer.config is not None


def test_app_inventory_not_empty():
    """Ensure the app inventory isn't empty"""
    assert app_deployer.app_inventory is not None
