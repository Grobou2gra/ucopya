#!/usr/bin/env python

import os.path
from distutils.core import setup

setup(
    name = 'ucopya',
    packages = ['ucopya'],
    scripts = ['bin/ucopya'],
    version = '0.1',
    author = 'Benoît Taine',
    author_email = 'ork@olol.eu',
    description = 'Interact with an Ucopia captive portal',
    url = 'https://github.com/ork/ucopya',
    install_requires=['requests>=2.4.0'],
    )
