#!/usr/bin/env python
# coding: utf-8
from setuptools import setup
from xsnippet_cli import __version__ as version


setup(
    name='xsnippet-cli',
    version=version,
    url='https://github.com/xsnippet/xsnippet-cli',
    license='BSD License',
    author='Igor Kalnitsky',
    author_email='igor@kalnitsky.org',
    description='A simple command line interface for the XSnippet service.',
    long_description=open('README.rst').read(),
    packages=['xsnippet_cli'],
    entry_points={
        'console_scripts': ['xsnippet = xsnippet_cli.cli:main'],
    },
    install_requires=[
        'Pygments>=1.5',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],
)
