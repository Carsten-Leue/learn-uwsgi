import cherrypy
from .utils import JSONType


@cherrypy.expose
@cherrypy.tools.json_out()
class ItemsResource(object):

    def GET(self) -> JSONType:
        return [{'a': 'b'}]


cherrypy.tree.mount(ItemsResource(), '/items', {
    '/': {
        'request.dispatch': cherrypy.dispatch.MethodDispatcher()
    }})
