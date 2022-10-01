k = int(input('Enter number: '))
Fibonacci = []

def fib(a):
    if a in [1, 2]:
        return 1
    elif a > 2:
        return fib(a - 1) + fib(a - 2)
    else:
        return fib(a + 2) - fib(a + 1)

for i in range(-k, k + 1):
    Fibonacci.append(fib(i))

print(Fibonacci)