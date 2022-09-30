s = int(input('Size of list = '))

lst = []

for i in range(s):
    lst.append(float(input(f'lst[{i}] = ')))


max_ = round(lst[0] % 1, 7)
min_ = round(lst[0] % 1, 7)

for i in range(s):
    k = round(lst[i] % 1, 7)
    if k != 0:
        if max_ < k:
            max_ = k

        elif min_ > k:
            min_ = k

print(round((max_ - min_), 7))