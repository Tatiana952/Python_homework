

def stud(r):
    if r == 1:
        dict = {1: "Понедельник",\
            2: "Вторник",\
            3: "Среда",\
            4: "Четверг"}
        day = int(input('\nВыберите день\
            \n1. Понедельник   2. Вторник   3.Среда   4.Четверг\nДень: '))
        with open('rasp.txt', 'r', encoding = 'utf-8') as rasp:
            lst = list(map(lambda x: x.replace('\n', ''), rasp.readlines()))
        for i in range(len(lst)):
            if dict[day] in lst[i]:
                while lst[i] != '':
                    print(lst[i])
                    print('---------------------------')
                    if i < len(lst)-1:
                        i += 1
                    else:
                        break
    elif r == 2:
        with open('homework.txt', 'r', encoding = 'utf-8') as rasp:
            lst = list(map(lambda x: x.replace('\n', ''), rasp.readlines()))
        dict = {1: "Русский язык",\
            2: "Физика",\
            3: "Ангийский язык",\
            4: "География",\
            5: "Информатика"}
        pr = int(input(f'\nВыбери предмет\
            \n 1. {dict[1]}   2. {dict[2]}   3. {dict[3]}   4.{dict[4]}   5.{dict[5]}\
            \n'))
        for i in range(len(lst)):
            if dict[pr] in lst[i]:
                print(lst[i])
    elif r == 3:
        with open('classes.txt', 'r', encoding = 'utf-8') as rasp:
            lst = list(map(lambda x: x.replace('\n', ''), rasp.readlines()))
        print("\nВыберите класс:")
        lst2 = []
        for i in range(len(lst)):
            if "-" in lst[i]:
                lst2.append(lst[i])
                print(lst[i])
        clas = input('Класс: ')
        while clas not in lst2:
            clas = input('Введите класс корректно: ')
        for i in range(len(lst)):
            if clas == lst[i]:
                while lst[i] != "":
                    print(lst[i])
                    if i < len(lst)-1:
                        i += 1
                    else:
                        break