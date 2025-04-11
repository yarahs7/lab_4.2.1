from flaskr import pages
from flaskr.backend import Backend

from flask import Flask, render_template, request, redirect, url_for

import logging

logging.basicConfig(level=logging.DEBUG)


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev',)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        # this file is not committed. Place it in production deployments.
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    backend = Backend()

    pages.make_endpoints(app, backend)

    return app
