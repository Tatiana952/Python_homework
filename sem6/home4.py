'''
Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''

# s = int(input('Size of list = '))

# lst1 = []
# lst2 = []

# for i in range(s):
#     lst1.append(int(input(f'lst1[{i}] = ')))

# for j in range((s // 2) + 1):
#     lst2.append(lst1[j] * lst1[s - 1 - j])

# print(f'\n{lst2}')

s = int(input('Size of list = '))

lst1 = []
lst2 = []

for i in range(s):
    lst1.append(input(f'lst1[{i}] = '))

lst1 = list(map(int, lst1))
lst2 = [lst1[j] * lst1[s - 1 - j] for j in range((s // 2) + 1)]

print(f'\n{lst2}')