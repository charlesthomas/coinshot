#!/usr/bin/env python
from distutils.core import setup
from os.path import dirname, join

NAME = 'coinshot'
VERSION = open( join( dirname( __file__ ), 'VERSION' ) ).read()
DESCRIPTION = 'simple python module for pushover.net'

setup(
    name = NAME,
    version = VERSION,
    description = DESCRIPTION,
    author = 'Charles Thomas',
    author_email = 'ch@rlesthom.as',
    url = 'http://bitbucket.org/charlesthomas/%s' % NAME,
)
