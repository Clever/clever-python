#!/bin/bash

# Publishes package to pypi and creates git tags.
# Reads version from VERSION file.
#
# To register a package (before first publish):
#   python setup.py register

version=`cat VERSION`
read -p "Publish and tag as v$version? " -n 1 -r
if [[ $REPLY =~ ^[Yy]$ ]]; then
  # publish to pypi
  python setup.py sdist upload

  # create git tags
  git tag -a v$version -m "version $version"
  git push --tags
fi
