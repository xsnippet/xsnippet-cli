# coding: utf-8
"""
    xsnippet_cli
    ~~~~~~~~~~~~

    XSnippet CLI is a simple command line interface for interacting
    with XSnippet service. Currently, it provides only posting and
    receiving snippets as a Guest user.

    You can send a file in the following way::

        $ xsnippet /path/to/file

    For sending a some command output, you can use a unix pipe system::

        $ ls -la | xsnippet

    If you want to retrieve a some snippet from the server, just do the
    following command::

        $ xsnippet -r <snippet id>

    The script provides a some useful options such as tags or language.
    Use ``$ xsnippet --help`` for more details.

    :copyright: (c) 2013 by Igor Kalnitsky.
    :license: BSD, see LICENSE for more details.
"""

__version__ = '0.1.0'
