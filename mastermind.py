from random import randint

def check4four(f):
    def inner(self, lst):
        if len(lst) != 4:
            raise ValueError, "sorry, wrong length of argument (should be 4)"
        ret = f(self, lst)
        return (ret)
    return (inner)

class A:
    def __init__(self, _alphabeth):
        self.alphabeth = _alphabeth

    def word(self, length = 4):
        return ( [ self.alphabeth[randint(0, len(self.alphabeth) - 1 )] for i in range(length)] )

class Board:
    @check4four
    def __init__(self, _secret):
        self.__secret = _secret

    @check4four
    def check(self, _request):
        cap = [(s == r) for s,r in zip(self.__secret, _request)]#.count(True)

        try:
            (s_temp, r_temp) = zip(*[(s,r) for s,r in zip(self.__secret, _request) if (s != r)])
            c = [(s in list(r_temp)) for s in list(s_temp)]#.count(True)
        except:
            c = []

        return ((cap.count(True), c.count(True)))


def genTree(_a, depth = 4):
    def _genTree(_a, _depth):
        if _depth > 0:
            return([(_a.alphabeth[i], _genTree(_a, (_depth-1))) for i in range(len(_a.alphabeth))])
        else:
            return([])

    return (("", _genTree(_a, depth)))
    
def leafs(_tree):
    value    = _tree[0]
    subtrees = _tree[1]

    if len(subtrees) == 0:
        return ([str(value)])

    return ([(str(value) + leaf) for subtree in subtrees for leaf in leafs(subtree)])
 
