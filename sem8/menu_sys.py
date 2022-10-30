#Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы
from schoolar import stud
from teacher import teach
from header import head

def main_menu():
    bb = False
    while bb == False:
        print('\nДобро пожаловать! Выберите режим работы:')
        print('1. Ученик    2. Учитель   3. Завуч   4. Выход из программы')
        r = int(input('Режим: '))

        if r == 4: bb = True
        elif r == 1:
            any = 1
            while any == 1:
                print('\nВыберите действие: ')
                print('1. Посмотреть расписание\n2. Посмотреть ДЗ\
                \n3. Список моего класса')
                a = int(input("Действие: "))
                stud(a)
                any = int(input('\nХотите что-то ещё?\n1. Да   2. Нет\nОтвет: '))
        elif r == 2:
            pass_ = input("Введите пароль: ")
            p = 0
            while pass_ != 't45':
                if p == 3:
                    print('Попытки исчерпаны')
                    break
                else:
                    pass_ = input(f"Пароль неверен. Осталось {3-p} попыток. Введите пароль: ")
                    p += 1
            else:
                any = 1
                while any == 1: 
                    print('Выберите действие: ')
                    print('1. Задать новое ДЗ    2. Посмотреть 2 последних сообщения от завуча')
                    a = int(input("Действие: "))
                    teach(a)
                    any = int(input('\nХотите что-то ещё?\n1. Да   2. Нет\nОтвет: '))
        elif r == 3:
            pass_ = input("\nВведите пароль: ")
            p = 0
            while pass_ != 'z90':
                if p == 3:
                    print('Попытки исчерпаны')
                    break
                else:
                    pass_ = input(f"Пароль неверен. Осталось {3-p} попыток. Введите пароль: ")
                    p += 1
            else:
                any = 1
                while any == 1:
                    print('\nСоздать новое сообщение учителям?')
                    any = int(input("Действие: \n1.Да    2.Нет\n"))
                    if any == 1:
                        head()
                    else: any = int(input('\nХотите что-то ещё?\n1. Да   2. Нет\nОтвет: '))


main_menu()