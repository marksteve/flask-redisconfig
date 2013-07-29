=================
Flask-RedisConfig
=================

Redis-backed config for Flask applications based on the `disqus/durabledict <https://github.com/disqus/durabledict>`_ library

-----
Usage
-----
::

    from flask import Flask
    from flask.ext.redisconfig import RedisConfig

    app = Flask(__name__)
    config = RedisConfig('app:config')
    config.init_app(app)

----------------------
Command Line Interface
----------------------
A CLI utility is provided for setting or reviewing config values easily.

::

    config.cli()

::

    Flask-RedisConfig
    > help

    Documented commands (type help <topic>):
    ========================================
    exit  get  help  list  set  set_bool  set_int

    > set SECRET_KEY oo5thuj4kaem2Pai0iviefahkaShah5iemae8Aev
    > get SECRET_KEY
    SECRET_KEY = 'oo5thuj4kaem2Pai0iviefahkaShah5iemae8Aev'
    > set_bool PRESERVE_CONTEXT_ON_EXCEPTION False
    > set_int SQLALCHEMY_POOL_SIZE 100
    > list
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SECRET_KEY = 'oo5thuj4kaem2Pai0iviefahkaShah5iemae8Aev'
    SQLALCHEMY_POOL_SIZE = 100
    >

-------
Example
-------
::
    $ python example.py config
    $ python example.py

-------
License
-------
http://marksteve.mit-license.org
