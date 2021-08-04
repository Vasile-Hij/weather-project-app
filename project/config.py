#!/bin/usr/env python3
from configparser import ConfigParser
import os

path = '/'


def createConfig(path):
    """
        Create the config file
    """
    config = ConfigParser()

    config['settings'] = {
        'debug': 'true',
        'secrete_key': '<secret_key>',
        'log_path': '/project'
    }

    config['db'] = {
        'db_name': 'weather_app-with-flask',
        'db_host': 'localhost',
        'db_port': '5000'
    }

    config['files'] = {
        'use_cdn': 'false',
        'images_path': '/project'
    }

    config['openweathermap'] = {
        'api': '<api_key>'
    }

    config['units'] = {
        'unit': 'metric'
    }

    config['SQLALCHEMY_DATABASE_URI'] = {
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///database.db'
    }

    with open('./config.ini', 'w') as f:
        config.write(f)


def crudConfig(path):
    """
    Create, read, update, delete config
    """
    if not os.path.exists(path):
        createConfig(path)

    config = ConfigParser.ConfigParser()
    config.read(path)


def interpolationDemo(path):
    """
    Interpolation: using options to build another option
    """
    if not os.path.exists(path):
        createConfig(path)

    config = ConfigParser.ConfigParser()
    config.read(path)


def main():
    createConfig(path)


if __name__ == '__main__':
    main()
