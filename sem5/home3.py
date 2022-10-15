place = [1, 2, 3, 4, 5, 6, 7, 8, 9]

win = [[0, 1, 2], [2, 5, 8], [3, 4, 5], [6, 7, 8], [1, 4, 7], [0, 3, 6], [0, 4, 8], [2, 4, 6]]

def prin_t(m):
    print(m[0], end = " ")
    print(m[1], end = " ")
    print(m[2])
    print(m[3], end = " ")
    print(m[4], end = " ")
    print(m[5])
    print(m[6], end = " ")
    print(m[7], end = " ")
    print(m[8]) 

def winner():
    w = ''
    for i in win:
        if place[i[0]] == 'X' and place[i[1]] == 'X' and place[i[2]] == 'X':
            w = 'X wone'
        elif place[i[0]] == '0' and place[i[1]] == '0' and place[i[2]] == '0':
            w = '0 wone'
    return w

game_over = False
player1 = True

while game_over == False:
    prin_t(place)
    if player1 == True:
        p = int(input('Where do you want to place X: '))
        place[p - 1] = 'X'
    else:
        p = int(input('Where do you want to place 0: '))
        place[p - 1] = '0'
    
    print('')
    res = winner()

    if res == '':
        game_over = False
        player1 = not(player1)
    else:
        game_over = True

print(res)
