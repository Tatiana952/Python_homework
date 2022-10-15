from random import randint

print('Choose gaming mode: \n \
    1. 2 people \n \
    2. Person and bot')

r = int(input('Mode = '))
c = 100 #number of candies2

def regimes(p, k):
    if p == 1:
        id = randint(1,2)

        print(f'There are {k} candies \n')

        while k > 0:

            igr = input(f"Number of candies for player {id} = ")

            def error(x, i, amount):
                while not x.isdigit() or int(x) > 28 or int(x) > amount:
                    if ',' in x or '.' in x:
                        x = input(f"\nEnter integer number of candies for player {i} = ")
                    elif not x.isdigit():
                        x = input(f"\nEnter the number of candies in numbers for player {i} = ")
                    elif int(x) > 28:
                        x = input(f"\nNumber of candies must be less than 28.\
                            Enter the number of candies in numbers for player {i} = ")
                    elif int(x) > amount:
                        x = input(f"\nNumber of candies must be less than {amount}.\
                        Enter the number of candies in numbers for player {i} = ")
                return x

            igr = int(error(igr, id, k))
            k -= igr
            print(f'There are {k} candies left')
            if k == 0:
                id = id
            elif id == 1:
                id = 2
            elif id == 2:
                id = 1

        print(f'Game over. Player {id} wone')
    else:
        # bot id = 1
        # person id = 2
        id = randint(1,2)
        
        print(f'There are {k} candies \n')

        while k > 0:
            if id == 2:
                igr = input(f"Number of candies for player {id} = ")

                def error(x, i, amount):
                    while not x.isdigit() or int(x) > 28 or int(x) > amount:
                        if ',' in x or '.' in x:
                            x = input(f"\nEnter integer number of candies for player {i} = ")
                        elif not x.isdigit():
                            x = input(f"\nEnter the number of candies in numbers for player {i} = ")
                        elif int(x) > 28:
                            x = input(f"\nNumber of candies must be less than 28.\
                                Enter the number of candies in numbers for player {i} = ")
                        elif int(x) > amount:
                            x = input(f"\nNumber of candies must be less than {amount}.\
                            Enter the number of candies in numbers for player {i} = ")
                    return x

                igr = int(error(igr, id, k))
                k -= igr
                print(f'There are {k} candies left')
            else:
                if k <= 28:
                    igr = k
                    print(f'Number of candies for player {id} = {igr}')
                elif  30 <= k <= 58:
                    igr = k - 29
                    print(f'Number of candies for player {id} = {igr}')
                else:
                    igr = randint(1,28)
                    print(f'Number of candies for player {id} = {igr}')
                k -= igr
                print(f'There are {k} candies left')

            if k == 0:
                id = id
            elif id == 1:
                id = 2
            elif id == 2:
                id = 1


        print(f'Game over. Player {id} wone')

regimes(r, c)