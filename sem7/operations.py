
def mult(rr):
    if rr[0] == '1':
        for i in range(2,4):
            rr[i] = float(rr[i])
        return rr[2] * rr[3]
    else:
        lst = []
        for i in range(2,4):
            lst.append(rr[i])
        print(lst)
        for i in range(0, len(lst)):
            lst[i] = lst[i].split(rr[i-2])
        print(lst)

t = ('-', '+', '6-7i', '-5+10i') 
mult(t)