
def fact(n):
    p = 1
    lst = []
    for i in range(1, n+1):
        p *= i
        lst.append(p)
    print(lst)

a = int(input('Enter a = '))
fact(a)