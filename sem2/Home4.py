N = int(input('Enter N = '))
a = int(input('Enter position a = '))
b = int(input('Enter position b = '))

lst = []
for i in range(-N, N + 1):
    lst.append(i)

print(lst)
print('lst[a] * lst[b] =', lst[a-1] * lst[b-1])