# coding: utf-8
"""
    xsnippet_cli
    ~~~~~~~~~~~~

    **xsnippet-cli** is a simple command line interface for interacting with
    Xsnippet_ service. By means this script, you can easily post and receive
    Snippets directly from your terminal.


    Usage
    -----

    It's very easy to use. You can paste the snippet this way ::

        $ xsnippet /path/to/file

    Or this way ::

        $ cat /path/to/file | xsnippet

    As you can see the last method posts a some command output. It's very
    usefull To post the last few lines from logfile this way ::

        $ tail -n 5 nginx.log | xsnippet

    It's important to note that you can specify a snippet language or tags.
    Thats can be done by the following command ::

        $ cat setup.py | xsnippet -l python -t setuptools test


    :copyright: (c) 2013 by Igor Kalnitsky.
    :license: BSD, see LICENSE for more details.
"""

__version__ = '0.1.1'
