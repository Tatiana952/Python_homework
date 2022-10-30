
def head():
    with open('message.txt', 'a', encoding = 'utf-8') as mess:
        print('Введите сообщение в формате: Дата(дд.мм.гггг) - Текст сообщения')
        m = input('Сообщение: ')
        mess.writelines(m + '\n')