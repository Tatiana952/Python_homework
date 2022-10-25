import imp
from  exp import export
from im import import_
from look_all import show
from add_con import add

b = False

while b == False: 
    print("\nWhat do you want to do?")
    print("1. Show all contacts\n2. Add contact\n3. Import contacts\n4. Export contacts\n5. End programm")
    p = int(input('Answer = '))

    if p == 5:
        b = True
    elif p == 1:
        show()
    elif p == 2:
        add()
    elif p == 3:
        import_()
    elif p == 4:
        export()
