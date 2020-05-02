from learn_uwsgi.encoder import CustomJSONEncoder
from typing import Optional
from ..iplink.api import IpLink
import cherrypy
from ..utils import JSONType


def createIplinkResource(ipLink: IpLink):

    encoder = CustomJSONEncoder()

    @cherrypy.expose
    @cherrypy.tools.json_out()
    class IplinkResource(object):

        def GET(self, name: Optional[str] = None) -> JSONType:            
            return encoder.default(ipLink.show(name))

    return IplinkResource()
