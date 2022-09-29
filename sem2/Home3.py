n = int(input())

def f(a):
    lst = []
    s = 0
    for i in range(1, a + 1):
        lst.append((1 + 1 / i)**i)
        s = s + lst[i-1]
    print(round(s, 3))

f(n)