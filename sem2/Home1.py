a = input('Enter a = ')

def f(n):
    s = 0
    if ',' in n:
        n = n.replace(',', '')
        n = int(n)
    elif '.' in n:
        n = n.replace('.', '')
        n = int(n)
    else:
        n = int(n)
    while n / 10 >= 0.1:
        s += n % 10
        n //= 10
    print(s)

f(a)
