
def add():
    d = {1: 'surname',
        2: 'name',
        3: 'telephone num.',
        4: 'description'}
    lst = []
    for i in range(1, len(d)+1):
        lst.append(input(f'Enter {d.get(i)}: '))
    with open('Base.txt', 'a', encoding='utf-8') as f:
        f.write('\n')
        f.write('\n')
        for i in range(len(lst)):
            if i == len(lst)-1:
                f.write(lst[i])
            else: 
                f.write(lst[i] + '\n')