import os

import cherrypy
from jinja2 import Environment, FileSystemLoader

from nifty_scraper import write_to_redis, read_from_redis

env = Environment(loader=FileSystemLoader('html'))


class NiftyFifty(object):
    @cherrypy.expose
    def index(self):
        time, data = read_from_redis()
        nifty_data = {
            'data': data,
            'time': time,
        }
        tmpl = env.get_template('index.html')
        return tmpl.render(**nifty_data)


if __name__ == '__main__':

    # update redis every 5 minutes i.e 300 seconds
    cherrypy.engine.housekeeper = cherrypy.process.plugins.BackgroundTask(300, write_to_redis)
    cherrypy.engine.housekeeper.start()

    config = {
        'global': {
            'server.socket_host': '0.0.0.0',
            'server.socket_port': int(os.environ.get('PORT', 5000)),
        },
        '/assets': {
            'tools.staticdir.root': os.path.dirname(os.path.abspath(__file__)),
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'assets',
        }
    }

    cherrypy.quickstart(NiftyFifty(), '/', config=config)
