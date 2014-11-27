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
        cAp = 0
        c   = 0
        tmp_request = _request
        tmp_secret = self.__secret
        for pos,col in enumerate(tmp_request):
            if tmp_secret[pos] == col:
                cAp += 1
                del(tmp_secret[pos])
                del(tmp_request[pos])
        for pos,col in enumerate(tmp_request):
            if col in tmp_secret:
                c   += 1
        return ((cAp, c))


