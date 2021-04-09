#!/usr/bin/env python
from setuptools import setup

NAME = 'coinshot'
DESCRIPTION = 'simple python module for pushover.net'
VERSION = open('VERSION').read().strip()
LONG_DESC = open('README.rst').read()
LICENSE = "MIT License"

setup(
    name=NAME,
    version=VERSION,
    author='Charles Thomas',
    author_email='ch@rlesthom.as',
    packages=['coinshot'],
    url='https://github.com/charlesthomas/%s' % NAME,
    license=LICENSE,
    description=DESCRIPTION,
    long_description=LONG_DESC,
    long_description_content_type='text/x-rst',
    install_requires=["simplejson >= 3.3.0"],
    scripts=['bin/shoot'],
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Intended Audience :: Developers',
                 'Intended Audience :: End Users/Desktop',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: MacOS :: MacOS X',
                 'Operating System :: POSIX :: Linux',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Topic :: Communications',
                 'Topic :: Software Development :: Libraries :: Python Modules']
)
