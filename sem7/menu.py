from get_num import get_numbers
from operations import mult
from operations import sum
from operations import diff
from operations import div

print('This is a calculator. It supports operations like: *, /, +, -')

end = False

while end == False:
    r = get_numbers()
    #print(r)

    if r[0] == '1':
        print('\nWhat operation do you choose?\n\
        1. a + b   2. a - b   3. a * b   4. a / b')
        op = int(input('Operation = '))
    else:
        print('\nWhat operation do you choose?\n\
        1. a + b   2. a - b   3. a * b')
        op = int(input('Operation = '))
    
    if op == 3:
        mult(r)
    elif op == 1:
        sum(r)
    elif op == 2:
        diff(r)
    else:
        div(r)

    wish = input('\nDo you want to continue?\n1.Yes    2.No\nAnswer = ')
    if int(wish) == 1:
        end = False
    else:
        end = True
