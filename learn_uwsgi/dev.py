from learn_uwsgi.iplink.mock import createIpLinkMock
from learn_uwsgi.iplink.shell import createIpLinkShell
from logging import Logger
from learn_uwsgi.routes import create_routes


def create_dev_routes(logger: Logger):
    create_routes(createIpLinkMock(logger))
