n = int(input('Enter number: '))
s = ''

while n / 2 >= 1:
    s = s + str(n - (n // 2) * 2)
    n = n // 2
else:
    s = s + str(n)

print(s[::-1])