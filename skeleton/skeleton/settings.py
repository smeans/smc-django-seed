# Django settings for skeleton project.
# This settings system is designed to make it easier to separate production
# settings from development settings. Do not modify this file, instead
# put all common configuration settings in settings_common.py. Then,
# put environment-specific settings (like database settings, template paths,
# urls, etc.) in a file that corresponds to the target environment (i.e.
# settings_development.py, settings_production.py). Then add the node() names
# for each target machine into the corresponding SETTINGS_MATRIX list.

import sys, importlib
from platform import node

from settings_common import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SETTINGS_MATRIX = {
    'production' : [],
    'staging' : [],
    'development': ['Scotts-iMac.local']
}

run_config = None

for k in SETTINGS_MATRIX:
    if node() in SETTINGS_MATRIX[k]:
        run_config = k

if run_config:
    print 'run configuration: %s' % run_config
    exec 'from %s_%s import *' % (__name__, run_config)
else:
    print 'WARNING: no run_config located for node \'%s\'' % node()
