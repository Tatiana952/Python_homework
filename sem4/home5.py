
from dataclasses import replace
from inspect import isdatadescriptor

# форма записи должна быть такой:
# -15x^4 - 3x^2 + 4x - 6 = 0
# 45x^3 - 9x^2 + x + 55 = 0

with open('1.txt') as f1:
    s1 = f1.readline()

with open('2.txt') as f2:
    s2 = f2.readline()

s1 = s1.replace(' = 0', '')
s1 = s1.replace('^', '')
s2 = s2.replace(' = 0', '')
s2 = s2.replace('^', '')

s1 = s1.split()
s2 = s2.split()

def f(lstt = []):
    i = 0
    while i < len(lstt):
        if lstt[i] == '-':
            lstt[i] += lstt[i+1]
            lstt.pop(i+1)
        elif lstt[i] == '+':
            lstt.pop(i)
        i += 1
    return(lstt)

s1 = f(s1)
s2 = f(s2)
#7x^4 + 45x^3 - 9x^2
Fs1 = s1[0].split('x')
Fs2 = s2[0].split('x')

if Fs1[1] == '' and Fs2[1] != '':
    max_st = int(Fs2[1])
elif Fs2[1] == '' and Fs1[1] != '':
    max_st = int(Fs1[1])
elif Fs1[1] == '' and Fs2[1] == '':
    max_st = 1
elif int(Fs1[1]) < int(Fs2[1]): 
    max_st = int(Fs2[1])
elif int(Fs1[1]) >= int(Fs2[1]):
    max_st = int(Fs1[1])

s1 += s2
print(s1)

s = ''
ee = []
ost = 0

for i in range(len(s1)): 
    if 'x' not in s1[i]:
        ost += int(s1[i])

while max_st > 1:
    for i in range(len(s1)):
        r = 'x' + str(max_st)
        if r in s1[i]:       
            s1[i] = s1[i].replace('x' + str(max_st), '')
            if s1[i] == '-':
                ee.append(-1)
            elif s1[i] == '':
                ee.append(1)
            else:
                ee.append(int(s1[i]))
    if sum(ee) == 1:
        s += 'x^' + str(max_st) + ' + '
    elif sum(ee) == -1:
        s = s[:-1]
        s = s[:-1]
        s += '- x^' + str(max_st) + ' + '
    elif sum(ee) > 0 or len(s) == 0:
        s += str(sum(ee)) + 'x^' + str(max_st) + ' + '
    elif sum(ee) < 0 and len(s) > 1:
        s = s[:-1]
        s = s[:-1]
        s += "- " + str(sum(ee) * (-1)) + 'x^' + str(max_st) + ' + '
    ee = []
    max_st -= 1

for i in range(len(s1)):
    r = 'x'
    if r in s1[i]:
        s1[i] = s1[i].replace('x', '')
        if s1[i] == '':
            ee.append(1)
        else:
            ee.append(int(s1[i]))
if sum(ee) == 1:
    s += 'x' + ' + '
elif sum(ee) == -1:
    s = s[:-1]
    s = s[:-1]
    s += '- x' + ' + '
elif sum(ee) > 0 or len(s) == 0:
    s += str(sum(ee)) + 'x' + ' + '
elif sum(ee) < 0 and len(s) > 1:
    s = s[:-1]
    s = s[:-1]
    s += "- " + str(sum(ee) * (-1)) + 'x' + ' + '
ee = []

if ost > 0:
    s += str(ost) + ' = 0'
elif ost < 0:
    s = s[:-1]
    s = s[:-1]
    s += "- " + str(ost * (-1)) + ' = 0'


print(s)