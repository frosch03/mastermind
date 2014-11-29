import cherrypy
import json
import mastermind
from mastermind import A


def withREST(o_class):
    @cherrypy.expose
    def get(self):
        cherrypy.response.headers['Content-Type'] = "application/json"
        return_dict = {}
        return_dict['board'] = {row[0] : row[1] for row in self.board}
        return_dict['state'] = "end" if self.ended else "running"
        return json.dumps(return_dict)
    
    @cherrypy.expose
    @cherrypy.tools.json_in()
    def ask(self):
        data = cherrypy.request.json
        self.check(data["request"])
        return(self.get())

    o_class.get = get
    o_class.ask = ask
    return(o_class)

Board = withREST(mastermind.Board)


if __name__ == '__main__':
    cherrypy.quickstart(Board((A("123456")).word()))
