data = 'aaaabccdeee'

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

print(sym)

for j in sym:
    for k in data:
        if j == k:
            count += 1
    str_ += j + str(count)
    count = 0

print(str_)
