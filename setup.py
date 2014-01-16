#!/usr/bin/env python
from setuptools import setup

NAME = 'coinshot'
DESCRIPTION = 'simple python module for pushover.net'
VERSION = open('VERSION').read().strip()
LONG_DESC = open('README.rst').read()

setup(
    name = NAME,
    version = VERSION,
    author = 'Charles Thomas',
    author_email = 'ch@rlesthom.as',
    packages = ['coinshot'],
    url = 'https://github.com/charlesthomas/%s' % NAME,
    license = 'MIT',
    description = DESCRIPTION,
    long_description = LONG_DESC,
    install_requires = ["simplejson >= 3.3.0"],
)
