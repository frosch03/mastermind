import cherrypy
import json
import mastermind
from   masterapi import A


def withREST(o_class):
    @cherrypy.expose
    def get(self):
        cherrypy.response.headers['Content-Type'] = "application/json"
        return_tuple = {row[0] : row[1] for row in self.board}
        return json.dumps(return_tuple)
    
    @cherrypy.expose
    def post(self, _request):
        self.check(_request)
        return(self.get())

    o_class.get  = get
    o_class.post = post
    return(o_class)

Board = withREST(mastermind.Board)


if __name__ == '__main__':
    cherrypy.quickstart(Board((A("123456")).word()))
