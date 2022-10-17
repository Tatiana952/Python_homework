'''
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
'''

# old
# data = 'aaaabccdeee'

# count = 0
# str_ = ''

# sym = []

# for i in range(len(data)):
#     if i < len(data) - 1 and data[i] != data[i + 1]:
#         sym.append(data[i])
#     elif i == len(data) - 1 and data[i] != data[i - 1]:
#         sym.append(data[i])
#     elif i == len(data) - 1 and data[i] == data[i - 1]:
#         sym.append(data[i])

# print(sym)

# for j in sym:
#     for k in data:
#         if j == k:
#             count += 1
#     str_ += j + str(count)
#     count = 0

# print(str_)


#new
mode = input('1. Compress data\n2. Recover data\nChoose mode = ')
data = input("Enter string: ")

if mode == '1': 
    count = 0
    str_ = ''
    sym = []

    for i in range(len(data)):
        if i < len(data) - 1 and data[i] != data[i + 1]:
            sym.append(data[i])
        elif i == len(data) - 1 and data[i] != data[i - 1]:
            sym.append(data[i])
        elif i == len(data) - 1 and data[i] == data[i - 1]:
            sym.append(data[i])

    for j in sym:
        for k in data:
            if j == k:
                count += 1
        str_ += j + str(count)
        count = 0

    print(str_)
else:
    lst1 = [data[i] for i in range(0, len(data)) if not data[i].isdigit()]
    lst2 = [data[i] for i in range(0, len(data)) if data[i].isdigit()]
    lst = list(zip(lst1, lst2))

    str_ = ''

    for i in enumerate(lst, start=0):
        l = i[1][0]
        n = int(i[1][1])
        for i in range(1, n+1):
            str_ += l

    print(str_)


