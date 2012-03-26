#!/usr/bin/env python
'shamelessly "borrowed" from https://github.com/dcramer/sentry/blob/master/runtests.py'
import base64
import logging
import os
import sys
from os.path import dirname, abspath
from optparse import OptionParser

sys.path.insert(0, dirname(abspath(__file__)))

logging.getLogger('autoauth').addHandler(logging.StreamHandler())

from django.conf import settings

if not settings.configured:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'autoauth.conf.default'

# override a few things with our test specifics
settings.INSTALLED_APPS = tuple(settings.INSTALLED_APPS) + (
    'tests',
)

from django_nose import NoseTestSuiteRunner


def runtests(*test_args, **kwargs):
    if 'south' in settings.INSTALLED_APPS:
        from south.management.commands import patch_for_test_db_setup
        patch_for_test_db_setup()

    if not test_args:
        test_args = ['tests']

    test_runner = NoseTestSuiteRunner(**kwargs)

    failures = test_runner.run_tests(test_args)
    sys.exit(failures)

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('--verbosity', dest='verbosity', action='store', default=1, type=int)
    parser.add_options(NoseTestSuiteRunner.options)
    (options, args) = parser.parse_args()

    runtests(*args, **options.__dict__)
