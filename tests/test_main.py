import unittest
import pytest

from app_deployer import __main__


def test_run_deploy_app_without_args(capsys):
    """Ensure a usage message is printed when running `deploy` without args"""
    with pytest.raises(SystemExit):
        __main__.main()
    out, err = capsys.readouterr()
    assert out and not err
