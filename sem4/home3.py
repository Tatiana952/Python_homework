lst = [3, 4, 5, 6, 6, 45, 3, 2, 2, 1, 0, 23, 89, 0, 90, 4]

for i in range(len(lst)):
    for j in range(len(lst)):
        f = True
        if lst[i] == lst[j] and i != j:
            f = False
            break
    if f == True:
        print(lst[i])