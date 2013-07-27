import cmd

from durabledict import RedisDict
from flask import current_app
from redis import Redis


class RedisConfig(RedisDict):
    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        key_prefix = app.config.get('REDISCONFIG_KEY_PREFIX')
        if not key_prefix:
            raise KeyError('REDISCONFIG_KEY_PREFIX is not defined')
        host = app.config.get('REDISCONFIG_HOST', 'localhost')
        port = app.config.get('REDISCONFIG_PORT', 6379)
        self.redis = Redis(host, port)
        autosync = app.config.get('REDISCONFIG_AUTOSYNC', True)
        super(RedisConfig, self).__init__(key_prefix, self.redis,
                                          autosync=autosync)

    def load(self):
        current_app.config.update(**self)

    def cli(self, app=None):
        if app:
            self.init_app(app)
        try:
            Cli(self).cmdloop()
        except KeyboardInterrupt:
            raise SystemExit


class Cli(cmd.Cmd, object):

    intro = 'Flask-RedisConfig'
    prompt = '> '

    def __init__(self, redisconfig):
        self.redisconfig = redisconfig
        super(Cli, self).__init__()

    def do_set(self, args, cast=str):
        """
        set KEY VALUE

        Sets a config value
        """
        try:
            key, value = args.split(' ')
            if cast == bool:
                if value.isdigit():
                    value = bool(int(value))
                else:
                    value = dict(true=True, false=False).get(value.lower())
                    if value is None:
                        raise ValueError
            else:
                value = cast(value)
            self.redisconfig[key] = value
        except ValueError:
            self.do_help('set')

    def do_set_int(self, args):
        """
        set_int KEY VALUE

        Sets a config integer value
        """
        self.do_set(args, cast=int)

    def do_set_bool(self, args):
        """
        set_bool KEY VALUE

        Sets a config boolean value
        """
        self.do_set(args, cast=bool)

    def do_get(self, args):
        """
        get KEY

        Gets a config value
        """
        try:
            key, = args.split(' ')
            if not key:
                raise ValueError
            self.redisconfig.sync()
            print '%s = %r' % (key, self.redisconfig.get(key))
        except ValueError:
            self.do_help('get')

    def do_list(self, args):
        """
        list

        Lists all config items
        """
        self.redisconfig.sync()
        for key, value in self.redisconfig.durables().iteritems():
            print '%s = %r' % (key, value)

    def do_help(self, args):
        """
        help

        Prints help stuff
        """
        super(Cli, self).do_help(args)

    def do_exit(self, args):
        """
        exit

        Quits cli
        """
        raise SystemExit
