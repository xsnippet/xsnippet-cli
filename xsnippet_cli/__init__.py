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
from __future__ import print_function

import os
import sys
import argparse

from pygments.lexers import get_lexer_for_filename
from xsnippet_cli import api


__version__ = '0.1.0'


def main():
    """
        An entry point of the command line interface.
    """
    args = _parse_arguments()

    if args.receive_id:
        return receive_snippet(args.receive_id)

    if args.filename:
        return post_file(args.filename, args.language, args.tags)
    else:
        return post_snippet(sys.stdin.read(), None, args.language, args.tags)


def post_file(filename, language, tags):
    title = os.path.basename(filename)

    if not language:
        language = get_lang_for_filename(filename)

    with open(filename) as f:
        post_snippet(f.read(), title, language, tags)


def post_snippet(content, title, language, tags):
    print(api.post_snippet(content, title, language, tags))


def receive_snippet(id_):
    print(api.get_snippet(id_))


def get_lang_for_filename(filename):
    try:
        aliases = get_lexer_for_filename(filename).aliases
        sname = aliases[0] if aliases else None
    except:
        sname = None
    return sname


def _parse_arguments():
    args = argparse.ArgumentParser(
        description='A simple command line interface for the XSnippet service.'
    )

    args.add_argument(
        'filename', nargs='?'
    )

    args.add_argument(
        '-r', '--receive', dest='receive_id',
        help='receive a snippet with a given id'
    )

    args.add_argument(
        '-t', '--tags', dest='tags', nargs='*',
        help='attach tags to the snippet'
    )

    args.add_argument(
        '-l', '--language', dest='language',
        help='attach language to the snippet'
    )

    return args.parse_args()
