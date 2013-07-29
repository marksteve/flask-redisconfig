from setuptools import setup

setup(
    name='Flask-RedisConfig',
    version='0.2.0',
    url='https://github.com/marksteve/flask-redisconfig',
    license='MIT',
    author='Mark Steve Samson',
    author_email='hello@marksteve.com',
    description='Redis-backed config for Flask applications',
    long_description=open('README.rst', 'r').read(),
    py_modules=['flask_redisconfig'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'durabledict',
        'redis',
    ],
    classifiers=[
    ],
)
