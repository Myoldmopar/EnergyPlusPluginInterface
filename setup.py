#!/usr/bin/env python

import codecs
import os
import setuptools

from epps import version


this_dir = os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(this_dir, 'README.rst'), encoding='utf-8') as i_file:
    long_description = i_file.read()

setuptools.setup(
    name='energyplus_epps',
    version=version,
    description='EnergyPlus Python Scripting Interface',
    long_description=long_description,
    url='https://github.com/nrel/energyplus',
    author='DOE',
    author_email='edwin.lee@nrel.gov',
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    keywords='python energyplus',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[],
    extras_require={},
    entry_points = {
        'console_scripts': ['test_script=epps.test_epps:main']
    }
)
