
def show():
    with open('Base.txt', 'r', encoding='utf-8') as b:
        k = b.readlines()
    k = list(map(lambda x: x.replace('\n', ''), k))
    print()
    for i in range(len(k)): 
        print(k[i])
