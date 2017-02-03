import os
import sys

try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

# Don't import clever module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'clever'))
import importer
import version

path, script = os.path.split(sys.argv[0])
os.chdir(os.path.abspath(path))

# Get simplejson if we don't already have json
install_requires = ['requests >= 0.8.8']
try:
  importer.import_json()
except ImportError:
  install_requires.append('simplejson')

try:
  import json
  _json_loaded = hasattr(json, 'loads')
except ImportError:
  pass

setup(name='clever',
      version=version.VERSION,
      description='Clever Python bindings',
      author='Clever',
      author_email='tech-support@clever.com',
      url='https://clever.com/',
      packages=['clever'],
      package_data={'clever' : ['data/clever.com_ca_bundle.crt', 'VERSION']},
      install_requires=install_requires,
      test_suite='test',
)
