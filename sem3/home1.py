s = int(input('Size of list = '))

lst = []

sum_ = 0

for i in range(s):
    lst.append(int(input(f'lst[{i}] = ')))
    if i % 2 != 0:
        sum_ += lst[i]

print(f'\nSum = {sum_}')