# -*- coding: utf-8 -*-

from distutils.core import setup

__author__ = "Sean Douglas"
__version__ = "0.1.0"
__license__ = "MIT"

setup(
    name='common_utils',
    version=__version__,
    author='Sean Douglas',
    author_email='seancdouglas@gmail.com',
    packages=['common_utils'],
    url='https://github.com/kiltlifter/common_utils',
    license='LICENSE.txt',
    description='Helpful python utilities',
    long_description=open('README.md').read(),
    install_requires=[],
    python_requires='>=3.6.0'
)

