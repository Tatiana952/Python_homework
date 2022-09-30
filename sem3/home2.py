s = int(input('Size of list = '))

lst1 = []
lst2 = []

for i in range(s):
    lst1.append(int(input(f'lst1[{i}] = ')))

for j in range((s // 2) + 1):
    lst2.append(lst1[j] * lst1[s - 1 - j])

print(f'\n{lst2}')