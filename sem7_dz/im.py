
def import_():
    print('\nChoose format for import.\n1. imp1.txt   2. imp2.txt')
    f = int(input('Format: '))

    if f == 1:
        with open('imp1.txt', 'r', encoding='utf-8') as file:  
            k = file.readlines()
            for i in range(len(k)):
                k[i] = k[i].split(', ')
            
        with open('Base.txt', 'a', encoding = 'utf-8') as b:
            b.write('\n')
            b.write('\n')
            for i in range(len(k)):
                for j in range(len(k[i])):
                    if i == len(k) - 1 and j == len(k[i]) - 1:
                        b.write(k[i][j])
                    else:
                        b.write(k[i][j] + '\n')
    elif f == 2:
        d = {0: 'Surname: ',
        1: 'Name: ',
        2: 'Tel.: ',
        3: 'Comm.: '}
        with open('imp2.txt', 'r', encoding='utf-8') as file:  
            k = file.readlines()
            for i in range(len(k)):
                for j in range(len(d)):
                    if d[j] in k[i]:
                        k[i] = k[i].replace(d[j], '')
        with open('Base.txt', 'a', encoding = 'utf-8') as b:
            b.write('\n')
            b.write('\n')
            for i in range(len(k)):
                    b.write(k[i])
