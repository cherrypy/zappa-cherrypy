import cherrypy


class Server:
    @cherrypy.expose
    def index(self):
        return 'Hello world!'


app = cherrypy.Application(Server(), '/dev/', {})


def main():
    cherrypy.tree.graft(app, '/dev/')
    cherrypy.server.unsubscribe()
    server = cherrypy._cpserver.Server()
    server.socket_host = '::'
    server.socket_port = 8080
    server.thread_pool = 30
    server.subscribe()
    cherrypy.engine.start()
    cherrypy.engine.block()


if __name__ == '__main__':
    main()
