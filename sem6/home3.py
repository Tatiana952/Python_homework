'''
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''


# s = int(input('Size of list = '))

# lst = []

# sum_ = 0

# for i in range(s):
#     lst.append(int(input(f'lst[{i}] = ')))
#     if i % 2 != 0:
#         sum_ += lst[i]

# print(f'\nSum = {sum_}')


s = int(input('Size of list = '))

lst = []
sum_ = 0

f = lambda x: x % 2 != 0

for i in range(s):
    lst.append(int(input(f'lst[{i}] = ')))
    if f(i):
        sum_ += lst[i]

print(lst)
print(f'\nSum = {sum_}')