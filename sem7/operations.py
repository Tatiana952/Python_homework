from logger import log_res

def change(lstt):
    if lstt[0] == "":
        lstt.pop(0)
        lstt[0] = "-" + lstt[0]
    
    lstt[1] = lstt[1].replace("i", "")
    if lstt[1] == "":
        lstt[1] = "1"
    elif lstt[1] == "-":
        lstt[1] = "-1"

def change2(rr, lst):
    if rr == "-":
        lst[len(lst)-1] = "-" + lst[len(lst)-1]

def mult(rr):
    if rr[0] == '1':     
        res = float(rr[2]) * float(rr[3])
        print(f"\na * b = {res}")
        log_res('a * b = ', res)
    else:
        lst1 = rr[2].split(rr[0])
        lst2 = rr[3].split(rr[1])

        change2(rr[0], lst1)
        change2(rr[1], lst2)

        change(lst1)
        change(lst2)

        lst1 = list(map(float, lst1))
        lst2 = list(map(float, lst2))

        lst = []
        lst.append(round(lst1[0] * lst2[0] - lst1[1] * lst2[1], 1))
        lst.append(round(lst1[0] * lst2[1] + lst1[1] * lst2[0], 1))

        res = str(lst[0])
        if lst[1] > 0:
            res += " + " + str(lst[1]) + "i"
        elif lst[1] < 0:
            res += str(lst[1]) + "i"
        elif lst[1] == 0:
            res = res
        
        log_res('a * b = ', res)
        print(f"\na * b = {res}")


def sum(rr):
    if rr[0] == '1': 
        res = float(rr[2]) + float(rr[3])      
        print(f"\na + b = {res}")
        log_res('a + b = ', res)
    else:
        lst1 = rr[2].split(rr[0])
        lst2 = rr[3].split(rr[1])

        change2(rr[0], lst1)
        change2(rr[1], lst2)

        change(lst1)
        change(lst2)

        lst1 = list(map(float, lst1))
        lst2 = list(map(float, lst2))

        lst = []
        lst.append(round(lst1[0] + lst2[0], 1))
        lst.append(round(lst1[1] + lst2[1], 1))

        res = str(lst[0])
        if lst[1] > 0:
            res += " + " + str(lst[1]) + "i"
        elif lst[1] < 0:
            res += str(lst[1]) + "i"
        elif lst[1] == 0:
            res = res

        print(f"\na + b = {res}")
        log_res('a + b = ', res)

def diff(rr):
    if rr[0] == '1':
        res = float(rr[2]) - float(rr[3])     
        print(f"\na - b = {res}")
        log_res('a - b = ', res)
    else:
        lst1 = rr[2].split(rr[0])
        lst2 = rr[3].split(rr[1])

        change2(rr[0], lst1)
        change2(rr[1], lst2)

        change(lst1)
        change(lst2)

        lst1 = list(map(float, lst1))
        lst2 = list(map(float, lst2))
        # print(lst1)
        # print(lst2)

        lst = []
        lst.append(round(lst1[0] - lst2[0], 1))
        lst.append(round(lst1[1] - lst2[1], 1))
        #print(lst)
        res = str(lst[0])
        if lst[1] > 0:
            res += " + " + str(lst[1]) + "i"
        elif lst[1] < 0:
            res += str(lst[1]) + "i"
        elif lst[1] == 0:
            res = res

        print(f"\na - b = {res}")
        log_res('a - b = ', res)

def div(rr):
    res = float(rr[2]) / float(rr[3])
    log_res('a / b = ', res)
    print(f"\na / b = {res}")

# t = ('+', '+', '1.28+i', '5.23+i') 
# mult(t)

