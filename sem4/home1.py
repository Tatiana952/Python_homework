
s1 = 0
s2 = 0
n = 0
d = 0.0001 #float(input('d = '))

while (s1 - s2) > d :
    n += 1
    print(n)
    s1 = s2 + (4 / (2 * n - 1))
    print(s1)
    n += 1
    print(n)
    s2 = s1 - (4 / (2 * n - 1))
    print(s2)


print((s1 + s2) / 2)