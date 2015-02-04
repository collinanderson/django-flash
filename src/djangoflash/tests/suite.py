# -*- coding: utf-8 -*-

"""Project's test suite.
"""
from __future__ import print_function
import os
import sys

# Adds the Django test project to system path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'testproj'))
sys.path.insert(0, os.path.dirname(__file__))
os.environ['DJANGO_SETTINGS_MODULE'] = 'testproj.settings'
import django
if hasattr(django, 'setup'):
    django.setup()

# Imports unit tests
from context_processors import *
from decorators import *
from models import *
from storage import *
from codec import *

# Now, the integration tests, which depends on SQLite
has_sqlite = True

try:
    import sqlite3
except ImportError:
    try:
        import pysqlite2
        has_sqlite = True
    except ImportError:
        pass

# Runs the integration tests if at least one module was found
if has_sqlite:
    # Bootstraps integration environment
    import django.test.utils as test_utils
    from django.db import connection
    test_utils.setup_test_environment()
    connection.creation.create_test_db()

    # Imports integration tests
    from testproj.app.tests import *
else:
    print('Integration: module "sqlite3" (or "pysqlite2") is required... SKIPPED', file=sys.stderr)
