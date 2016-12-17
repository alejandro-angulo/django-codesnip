import os
import sys
import django
import pytest

from django.conf import settings
from django.test.utils import get_runner

PYTEST_ARGS = ['--cov-report', 'html', '--cov', 'codesnip',
               'tests', '--tb=short', '-s', '-rw']


def runtests():
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.test_settings'
    django.setup()
    # TestRunner = get_runner(settings)
    # test_runner = TestRunner()
    # failures = test_runner.run_tests(*PYTEST_ARGS)
    # sys.exit(bool(failures))
    sys.exit(pytest.main(PYTEST_ARGS))


if __name__ == '__main__':
    runtests()
