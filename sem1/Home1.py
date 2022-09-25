a = int(input('Enter number of a day: '))

while a > 7 or a < 1:
    a = int(input('Enter number of a day: '))

if a == 7 or a == 6:
    print('\n yes')
else:
    print('\n no')