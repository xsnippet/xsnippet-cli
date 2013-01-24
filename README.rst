XSnippet CLI
============


Usage
-----

It's very easy to use. You can send a snippet via piping ``stdin`` or specifing
a desired file. For the first case you shold use something like that::

    $ df -h | xsnippet

For the second case, you should use the ``--send`` flag::

    $ xsnippet --send example.txt


