import cherrypy
import json
import mastermind
from mastermind import A

def withREST(o_class):
    o_class._cp_config = {'tools.CORS.on': True} 
    o_new = o_class.new
    @cherrypy.expose
    def new(self):
        o_new(self)
        return(self.get())
    o_class.new = new

    @cherrypy.expose
    def get(self):
        cherrypy.response.headers['Content-Type'] = "application/json"
        return_dict = {}
        return_dict['board'] = [{"move": tuple(row[0]), "result": row[1]} for row in self.board.board]
        return_dict['state'] = "end" if self.ended else "running"
        return json.dumps(return_dict)
    o_class.get  = get
    
    o_move = o_class.move
    @cherrypy.expose
    @cherrypy.tools.json_in()
    def move(self):
        data = cherrypy.request.json
        o_move(self, data["request"])
        return(self.get())
    o_class.move = move

    return (o_class)

Game = withREST(mastermind.Game)


def CORS():
    cherrypy.response.headers['Access-Control-Allow-Origin'] = "*"

if __name__ == '__main__':
    cherrypy.tools.CORS = cherrypy.Tool('before_finalize', CORS)
    cherrypy.tree.mount(Game([1,2,3,4,5,6]))
    cherrypy.server.socket_host = '10.0.101.42'
    cherrypy.engine.start()
    cherrypy.engine.block()