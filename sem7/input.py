
def enter(d):
    print('\nEnter value. Example for complex: -5-6i')
    a = input(f'Enter value {d} = ')
    return a

def ch_sym(str_):
    if '+' in str_:
        k = '+'
    elif '-' in str_:
        for i in range(1, len(str_)):
            if str_[i] == '-':
                k = '-'
                break
        else:
            k = '1' # if str_ = -3 
    else:
        k = '1' # if str_ = 3
    #print(k)

    return k