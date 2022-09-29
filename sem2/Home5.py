from random import randint

n = int(input('Enter size of list: '))

lst = []

for i in range(n):
    lst.append(randint(-100, 100))

print(lst)

for i in range(n):
    j = randint(0, i+1)
    a = lst[j]
    lst[j] = lst[i]
    lst[i] = a

print(lst)