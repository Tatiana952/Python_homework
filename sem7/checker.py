from logger import log_comm

def check_compl(data, z):
    log_comm('is complex')
    data = data.split(z)
    if data[0] == '':
        del data[0]
        data[0] = '-' + data[0]
    data[1] = data[1].replace('i', '')
    if data[1] == '':
        data[1] = '1'
    if z == '-':
        data[1] = z + data[1]
    for t in data[0]:
        if t != '-' and not t.isdigit():
            u1 = False
            break
    else:
        u1 = True
    for t in data[1]:
        if t != '-' and not t.isdigit():
            u2 = False
            break
    else:
        u2 = True
    if u1 == False or u2 == False:
        return False
    else:
        return True

def check_rac(data):
    log_comm('is rational')
    data = data.replace(',', '.')
    k = False
    for i in range(0, len(data)):
        if not data[i].isdigit() and data[i] != '.' and data[i] != '-':
            k = False
            break
    else:
        k = True
    return k
