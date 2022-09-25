x = int(input('Enter X = '))
y = int(input('Enter Y = '))

while x == 0 or y == 0:
    x = int(input('Enter X = '))
    y = int(input('Enter Y = '))

if x > 0 and y > 0:
    print ('\n I quarter')
elif x < 0 and y > 0:
    print ('\n II quarter')
elif x < 0 and y < 0:
    print ('\n III quarter')
else:
    print ('\n IV quarter')