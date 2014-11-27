
def check4four(f):
    def inner(self, lst):
        if len(lst) != 4:
            raise ValueError, "sorry, wrong length of argument (should be 4)"
        ret = f(self, lst)
        return (ret)
    return (inner)


class Board:
    @check4four
    def __init__(self, _secret):
        self.__secret = _secret

    @check4four
    def check(self, _request):
        cAp = 0
        c   = 0
        for pos,col in enumerate(_request):
            if col in self.__secret:
                c   += 1
            if self.__secret[pos] == col:
                cAp += 1
        return ((cAp, c))

