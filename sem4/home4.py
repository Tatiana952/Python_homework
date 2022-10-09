from random import randint, random


k = int(input('k = '))
str_ = ''
x = ''

while k >= 0:
    coeff = randint(0, 100)
    if coeff == 0 and k >= 1:
        k -= 1
    elif coeff > 0 and k > 0:
        if k > 1:
            k_str = str(k)
            for j in range(len(k_str)):
                if int(k_str[j]) == 2 or int(k_str[j]) == 3:
                    x1 = eval(r'"\u00b' + str(int(k_str[j])) + '"')
                elif 4 <= int(k_str[j]) <= 9:
                    x1 = chr(0x2070 + int(k_str[j]))
                elif int(k_str[j]) == 0:
                    x1 = chr(0x2070 + 0)
                else:
                    x1 = eval(r'"\u00b' + str(9) + '"')
                x += x1
            str_ = str_ + str(coeff) + 'x' + x + ' + '
        elif k == 1: 
            str_ = str_ + str(coeff) + 'x ' + '+ '
    elif coeff > 0 and k == 0:
        str_ = str_ + str(coeff) + " "
        
    k -= 1
    x = ''

if str_[-2] == "+":
    str_ = str_[:-1]
    str_ = str_[:-1]

str_ = str_ + '= 0'
print(str_)  
