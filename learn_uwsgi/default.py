from typing import List, Mapping, Tuple, Union

import cherrypy


@cherrypy.expose
class DefaultResource(object):

    def GET(self) -> str:
        return 'default'
