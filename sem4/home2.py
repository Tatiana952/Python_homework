n = int(input('N = '))

lst = []    

for i in range (2, n + 1):
    while n % i == 0:
        lst.append(i)
        n /= i

print(lst)