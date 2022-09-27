# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

k = 0

for x in range(2):
    for y in range(2):
        for z in range(2):
            if not (x and y and z):
                Left = str(x) + ' ' + str(y) + ' ' + str(z)
            if not(x) or not(y) or not(z):
                Right = str(x) + ' ' + str(y) + ' ' + str(z)
            if Left == Right:
                k = k + 1
            
if k == 2**3:
    print('\n Утверждение истинно')
else:
    print('\n Утверждение не истинно')