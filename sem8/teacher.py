
def teach(t):
    if t == 1:
        dict = {1: "Русский язык",\
            2: "Физика",\
            3: "Ангийский язык",\
            4: "География",\
            5: "Информатика",\
            6: "Литература"}
        pr = int(input(f'\nВыбери предмет\
            \n 1. {dict[1]}   2. {dict[2]}   3. {dict[3]}   4.{dict[4]}   5.{dict[5]}   6.{dict[6]}\
            \n'))
        dz = input('Введите текст домашнего задания: ')
        with open('homework.txt', 'r', encoding = 'utf-8') as rasp:
            lst = list(rasp.readlines())
        for j in range(len(lst)):
            if dict[pr] in lst[j]:
                lst[j] = f'{dict[pr]}: {dz}\n'
        with open('homework.txt', 'w', encoding = 'utf-8') as home:
            home.writelines(lst)
    elif t == 2:
        with open('message.txt', 'r', encoding = 'utf-8') as mess:
            lst = list(map(lambda x: x.replace('\n', ''), mess.readlines()))
        for i in range(len(lst)-2, len(lst)):
            print(lst[i])