#!/usr/bin/env python
from distutils.core import setup
from os.path import dirname, join

NAME = 'coinshot'
DESCRIPTION = 'simple python module for pushover.net'
VERSION = open( join( dirname( __file__ ), 'VERSION' ) ).read()

setup(
    name = NAME,
    version = VERSION,
    description = DESCRIPTION,
    author = 'Charles Thomas',
    author_email = 'ch@rlesthom.as',
    url = 'http://code.cha.rlesthom.as/%s' % NAME,
)
