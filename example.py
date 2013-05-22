import sys

from flask import Flask, jsonify
from flask.ext.redisconfig import RedisConfig


app = Flask(__name__)
app.config.update(REDISCONFIG_KEY_PREFIX='app:config')
config = RedisConfig(app)
config.load()


@app.route('/')
def index():
    redisconfig = config.durables()
    appconfig = {}
    for key in redisconfig.keys():
        appconfig[key] = app.config.get(key)
    return jsonify(redisconfig=redisconfig, appconfig=appconfig)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'cli':
        config.cli()
    else:
        app.run(debug=True)