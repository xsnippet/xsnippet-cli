# coding: utf-8
"""
    xsnippet_cli.cli
    ~~~~~~~~~~~~~~~~

    This module contains a command line interface for interacting
    with this script.

    :copyright: (c) 2013 by Igor Kalnitsky.
    :license: BSD, see LICENSE for more details.
"""
from __future__ import print_function

import os
import sys
import argparse

from pygments.lexers import get_lexer_for_filename
from xsnippet_cli import api


def main():
    """
        An entry point of the command line interface. The main
        purpose of this function is a job dispatching.
    """
    args = _parse_arguments()

    if args.receive:
        return _receive_snippet(args.receive)
    return _post_snippet(args.filename, args.caption, args.language, args.tags)


def _receive_snippet(snippet_id, _info=True):
    """
        Retrieve from the server a snippet with a given id
        and print it to ``stdout``.

        .. note: The function prints snippet info if the ``_info``
                 argument is True.
    """
    snippet = api.get_snippet(snippet_id)

    for key, value in snippet.items():
        if _info and value and key != 'content':
            print(':{key}: {value}'.format(key=key, value=value))

    print(snippet['content'])


def _post_snippet(filename=None, caption=None, language=None, tags=None):
    """
        Send a snippet with a given attributes to the server. If ``filename``
        is not specify the ``stdin`` will be post.

        .. note: If ``filename`` is specified the language will be defined
                 automatically. Please note, this feature will be activated
                 only if you not specify a language manually.
    """
    def get_file_info(filename, caption, language):
        with open(filename) as f:
            content = f.read()
        if not caption:
            caption = os.path.basename(filename)
        if not language:
            language = _get_lang_for_filename(filename)
        return content, caption, language

    if not filename:
        content = sys.stdin.read()
    else:
        content, caption, language = get_file_info(filename, caption, language)

    # post snippet and print a link to the posted snippet
    print(api.post_snippet(content, caption, language, tags))


def _get_lang_for_filename(filename):
    try:
        aliases = get_lexer_for_filename(filename).aliases
        sname = aliases[0] if aliases else None
    except:
        sname = None
    return sname


def _parse_arguments():
    """
        Parse command line arguments and returns result.
        Execute ``$ xsnippet --help`` for more details.
    """
    args = argparse.ArgumentParser(
        description='A simple command line interface for the XSnippet service.'
    )

    args.add_argument('filename', nargs='?')
    args.add_argument('-c', '--caption', dest='caption')
    args.add_argument('-t', '--tags', dest='tags', nargs='*')
    args.add_argument('-l', '--language', dest='language')
    args.add_argument('-r', '--receive', dest='receive', metavar='ID')

    return args.parse_args()
