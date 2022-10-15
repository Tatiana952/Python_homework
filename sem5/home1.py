with open('1.txt', 'r', encoding="utf-8") as f:
    r = f.readline().split()

print(list(filter(lambda x: 'абв' not in x, r)))