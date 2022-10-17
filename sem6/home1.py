'''
Задание 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

Пример:

пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
'''
#old 
# def fact(n):
#     p = 1
#     lst = []
#     for i in range(1, n+1):
#         p *= i
#         lst.append(p)
#     print(lst)

# a = int(input('Enter a = '))
# fact(a)


def fact(n):
    p = 1
    if n > 0:
        lst = [p := p*i for i in range(1, n+1)]
    elif n == 0:
        lst = [1]
    print(lst)

a = int(input('Enter a = '))
fact(a)
