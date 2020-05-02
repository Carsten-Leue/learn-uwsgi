import cherrypy
from learn_uwsgi.iplink.api import IpLink
from .controllers import createIplinkResource


def create_routes(ipLink: IpLink):

    cherrypy.tree.mount(createIplinkResource(ipLink), '/iplink', {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher()
        }})
