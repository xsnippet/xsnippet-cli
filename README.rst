xsnippet-cli
============

**xsnippet-cli** is a simple command line interface for interacting with
xsnippet_ service. By means this script, you can easily post and receive
snippets directly from your terminal.


Usage
-----

It's very easy to use. You can paste the snippet this way ::

    $ xsnippet /path/to/file

or this way ::

    $ cat /path/to/file | xsnippet

As you can see the last method posts a some command output. It's very usefull
to post the last few lines from logfile this way ::

    $ tail -n 5 nginx.log | xsnippet

It's important to note that you can specify a snippet language or tags.
Thats can be done by the following command ::

    $ cat setup.py | xsnippet -l python -t setuptools test


Installation
------------

::

    $ (sudo) pip install xsnippet-cli

or

::

    $ (sudo) easy_install xsnippet-cli

or

::

    $ wget http://git.io/xsnippet-cli.zip -O xsnippet-cli.zip
    $ unzip xsnippet-cli.zip && cd xsnippet-cli-master
    $ (sudo) python ./setup.py install


Meta
----

- Author: Igor Kalnitsky <igor@kalnitsky.org>
- License: BSD License


.. _xsnippet: http://xsnippet.org/
