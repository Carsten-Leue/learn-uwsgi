from learn_uwsgi.iplink.shell import createIpLinkShell
from logging import Logger
from learn_uwsgi.routes import create_routes


def create_prod_routes(logger: Logger):
    create_routes(createIpLinkShell(logger))
