Ch = int(input('Enter numer of quarter: '))

while Ch > 4 or Ch < 1:
    Ch = int(input('Enter numer of quarter: '))

if Ch == 1:
    print('X ' + chr(8712) + ' [0; +' + chr(8734) + ')')
    print('Y ' + chr(8712) + ' [0; +' + chr(8734) + ')')
elif Ch == 2:
    print('X ' + chr(8712) + ' [0; -' + chr(8734) + ')')
    print('Y ' + chr(8712) + ' [0; +' + chr(8734) + ')') 
elif Ch == 3:
    print('X ' + chr(8712) + ' [0; -' + chr(8734) + ')')
    print('Y ' + chr(8712) + ' [0; -' + chr(8734) + ')') 
else:
    print('X ' + chr(8712) + ' [0; +' + chr(8734) + ')')
    print('Y ' + chr(8712) + ' [0; -' + chr(8734) + ')') 
