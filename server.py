import cherrypy
import logging
from learn_uwsgi import DefaultResource, create_dev_routes

if __name__ == '__main__':

    create_dev_routes(logging.getLogger('root'))

    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher()
        } 
    }
    cherrypy.quickstart(DefaultResource(), '/', conf)
