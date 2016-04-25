import unittest

# Try to import app_deployer, which will execute the functions in __init__.py
from app_deployer import __main__

if __name__ == '__main__':
    import sys

    sys.exit(unittest.main())
