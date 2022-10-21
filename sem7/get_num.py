from input import enter
from input import ch_sym
from checker import check_compl
from checker import check_rac
from logger import log 

def get_numbers():
    aa = False
    while aa == False:
        a = enter('a')
        log('a', a)
        s1 = ch_sym(a)
        if not s1 == '1':
            aa = check_compl(a, s1)
        else:
            aa = check_rac(a)

    bb = False

    while bb == False:
        b = enter('b')
        log('b', b)
        s2 = ch_sym(b)
        if s1 == '1' and s2 != '1':
            bb = False
        elif not s2 == '1':
            bb = check_compl(b, s2)
        else:
            bb = check_rac(b)
    return s1, s2, a, b