#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob
from codecs import BOM

from setuptools import setup, find_packages
from setuptools.command.build_py import build_py as _build_py

VERSION = '0.1'

readme_file = open(u'README')
long_description = readme_file.read()
readme_file.close()
if long_description.startswith(BOM):
    long_description = long_description.lstrip(BOM)
long_description = long_description.decode('utf-8')

package_data = {
    '': ['LICENSE', 'README'],
}

setup(
    name="transifex-adofex",
    version=VERSION,
    description="Transifex addons for localizing Mozilla's extensions",
    long_description=long_description,
    author="Tim Babych",
    author_email="tim.babych@gmail.com",
    url="http://bitbucket.org/tymofiy/transifex-adofex",
    license="GPLv2",
    dependency_links = [],
    setup_requires = [],
    install_requires = [],
    data_files=[],
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    package_data = package_data,
    keywords = (
        'mozilla translation localization internationalization vcs',),
)
