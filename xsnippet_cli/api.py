# coding: utf-8
"""
    xsnippet_cli.api
    ~~~~~~~~~~~~~~~~

    This module provides a simple functions for interacting with
    XSnippet RESTful API.

    :copyright: (c) 2013 by Igor Kalnitsky.
    :license: BSD, see LICENSE for more details.
"""
import json
from functools import wraps

try:
    # python 3
    from urllib.request import urlopen
    from urllib.parse import urlencode
except ImportError:
    # python 2
    from urllib import urlencode
    from urllib2 import urlopen


class api(object):
    """
        A simple wrapper for setting ``_api`` url for a given function.

        Usage example::

            @api('/snippets/')
            def send_snippet(some1, some2, _api=None):
                pass
    """
    URL = 'http://xsnippet.org/api/v1'

    def __init__(self, resource):
        self.resource = resource

    def __call__(self, func):
        @wraps(func)
        def decorator(*args, **kwargs):
            kwargs['_api'] = api.URL + self.resource
            return func(*args, **kwargs)
        return decorator


def url_for_snippet(id_):
    return 'http://xsnippet.org/' + str(id_)


@api('/snippets/')
def post_snippet(content, title=None, language=None, tags=None, _api=None):
    """
        Send snippet with a given parameters to the service.
        Return url to the posted snippet if success; otherwise return None.
    """
    # the content should be not empty
    assert content
    # the api url should be defined
    assert _api

    # make data dict
    data = {
        'content': content,
        'title': title,
        'language': language,
        'tags': ','.join(tags) if tags else None,
    }

    # remove from data items with incorrect values
    # it's not a required step, but i want make a clean request :)
    data = {key: value for key, value in data.items() if value}

    try:
        # post snippet and return url to the posted snippet
        response = urlopen(_api, urlencode(data)).read()
        response = json.loads(response)
        return url_for_snippet(response.get('id'))
    except:
        # return None if something wrong
        return None


@api('/snippets/{id}')
def get_snippet(id_, _api=None):
    pass
