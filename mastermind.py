import cherrypy
import json
from random import randint

def check4four(f):
    def inner(self, lst):
        if len(lst) != 4:
            raise ValueError, "sorry, wrong length of argument (should be 4)"
        ret = f(self, lst)
        return (ret)
    return (inner)

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


class A:
    def __init__(self, _alphabeth):
        self.alphabeth = _alphabeth

    def word(self, length = 4):
        return ( [ self.alphabeth[randint(0, len(self.alphabeth) - 1 )] for i in range(length)] )



@withREST
class Board:
    @check4four
    def __init__(self, _secret, ttl = 9):
        self.__secret = _secret
        self.__ttl    = ttl
        self.board    = []
        self.__ended  = False

    def __str__(self):
        ret = ""
        for (r, a) in self.board:
            ret = ("\n[%c%c%c%c] -> [%i|%i]"%(str(r[0]), str(r[1]), str(r[2]), str(r[3]), a[0],a[1])) + ret
        return (ret[1:])

    @check4four
    def check(self, _request):
        if self.__ttl > 0 and not self.__ended:
            cap = [(s == r) for s,r in zip(self.__secret, _request)].count(True)
            try:
                (s_temp, r_temp) = zip(*[(s,r) for s,r in zip(self.__secret, _request) if (s != r)])
                c = [(s in list(r_temp)) for s in list(s_temp)].count(True)
            except:
                c = []

            self.board.append(( _request , (cap, c) ))
            self.__ttl -= 1
            if cap >= 4: self.__ended = True
            return str((cap, c))


class Solutions:
    def __init__(self, _a, depth = 4):
        self.__tree = ("", [])
        self.genTree(_a, depth)

    def genTree(self, _a, depth = 4):
        def _genTree(_a, _depth):
            if _depth > 0:
                return([(_a.alphabeth[i], _genTree(_a, (_depth-1))) for i in range(len(_a.alphabeth))])
            else:
                return([])
        self.__tree = (("", _genTree(_a, depth)))
        
    def solutions(self):
        def leafs(_tree):
            value    = _tree[0]
            subtrees = _tree[1]
        
            if len(subtrees) == 0:
                return ([str(value)])
        
            return ([(str(value) + leaf) for subtree in subtrees for leaf in leafs(subtree)])
        return(leafs(self.__tree))
    
    def delete(self, _char, pos = None):
        def inner_delete(_tree, _char, pos = None):
            value    = _tree[0]
            subtrees = _tree[1]
        
            if None == pos:
                return (value, [inner_delete(subtree, _char, None) for subtree in subtrees if subtree[0] != _char]) 
            else:
                return (value, [deleteAt(subtree, _char, pos-1) for subtree in subtrees if subtree[0] != _char or (pos-1) != 0])
        self.__tree = inner_delete(self.__tree, _char, pos)

class Game:
    def __init__(self, _chars):
        self.a     = A(_chars)
        self.board = Board(self.a.word())
        self.notes = Solutions(self.a)


if __name__ == '__main__':
    cherrypy.quickstart(Board((A("123456")).word()))
