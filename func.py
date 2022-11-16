import sympy
from sympy import Symbol 
from sympy import plot 
import matplotlib
from sympy import sin, cos 

x = Symbol('x')
f_x = -12*sin(cos(x))*x**4 - 18*x**3 + 5*x**2 + 10*x - 30
#print(f_x)

#plot(f_x)

f_x_dif = f_x.diff()
#print(f_x_dif)
#plot(f_x_dif)

#def root():
lst = []
# lst2 = [1, 10, 100, 1000, 10000, 100000]
k = 0
# #for j in range(len(lst2)):
# for i in range (-10,-4):
#     tup = (i, f_x.subs(x, i).evalf())
#     lst.append(tup)
#     #print(f" x = {lst[k][0]}  f(x) = {lst[k][1]}")
#     if lst[k][1] < 0 and lst[k-1][1] > 0:
#         begin = lst[k-1][0]
#         end = lst[k][0]
#         print(begin, end)
#         k +=1
#         break
#     # if solution > 0:
#     #     begin = solution
#     # else:
#     #     end = solution
#     k += 1


# print(begin*10, end*10)
# for i in range (begin*10,end*10):
#     i = i/10
#     tup = (i, f_x.subs(x, i).evalf())
#     lst.append(tup)
#     print(f" x = {lst[k][0]}  f(x) = {lst[k][1]}")
#     if lst[k][1] < 0 and lst[k-1][1] > 0:
#         begin = lst[k-1][0]
#         end = lst[k][0]
#         print(begin, end)
#         k +=1
#         break
#     k += 1

# for i in range (round(begin*100),round(end*100)):
#     i = i/100
#     tup = (i, f_x.subs(x, i).evalf())
#     lst.append(tup)
#     print(f" x = {lst[k][0]}  f(x) = {lst[k][1]}")
#     if lst[k][1] < 0 and lst[k-1][1] > 0:
#         begin = lst[k-1][0]
#         end = lst[k][0]
#         print(begin, end)
#         k +=1
#         break
#     k += 1



# for i in range (round(begin*1000),round(end*1000)):
#     i = i/1000
#     tup = (i, f_x.subs(x, i).evalf())
#     lst.append(tup)
#     print(f" x = {lst[k][0]}  f(x) = {lst[k][1]}")
#     if lst[k][1] < 0 and lst[k-1][1] > 0:
#         begin = lst[k-1][0]
#         end = lst[k][0]
#         break
#     if lst[k][1] > 0:
#         begin = lst[k][0]
#     k += 1
# print(begin, end)

# for i in range(round(begin*10000),round(end*10000)):
#     i = i/10000
#     tup = (i, f_x.subs(x, i).evalf())
#     lst.append(tup)
#     print(f" x = {lst[k][0]}  f(x) = {lst[k][1]}")
#     if lst[k][1] < 0 and lst[k-1][1] > 0:
#         begin = lst[k-1][0]
#         end = lst[k][0]
#         k += 1
#         break
#     k += 1
# print(begin, end)

# for i in range(round(begin*100000),round(end*100000)):
#     i = i/100000
#     tup = (i, f_x.subs(x, i).evalf())
#     lst.append(tup)
#     print(f" x = {lst[k][0]}  f(x) = {lst[k][1]}")
#     if lst[k][1] < 0 and lst[k-1][1] > 0:
#         begin = lst[k-1][0]
#         end = lst[k][0]
#         k += 1
#         break
#     k += 1
# print(begin, end)

# for i in range(round(begin*1000000),round(end*1000000)):
#     i = i/1000000
#     tup = (i, f_x.subs(x, i).evalf())
#     lst.append(tup)
#     print(f" x = {lst[k][0]}  f(x) = {lst[k][1]}")
#     if lst[k][1] < 0 and lst[k-1][1] > 0:
#         begin = lst[k-1][0]
#         end = lst[k][0]
#         k += 1
#         break
#     k += 1
# print(begin, end)


r = 0
b = -10
e = -4
def root(begin, end, r, f_x):
    k = 0
    lst = []
    for i in range(round(begin*10**r),round(end*10**r)):
        i = i/(10**r)
        y = f_x.subs(x, i).evalf()
        print(f"i = {i}; y = {y}")
        tup = (i, y)
        lst.append(tup)
        print(lst[k][1], lst[k-1][1])
        #print(f" x = {lst[k][0]}  f(x) = {lst[k][1]}")
        if lst[k][1] < 0 and lst[k-1][1] > 0:
            begin = lst[k-1][0]
            end = lst[k][0]
            k += 1
            break
        if lst[k][1] > 0:
            begin = lst[k][0]
    #print(begin, end)
    dif_1 = abs(lst[k-1][1])
    dif_2 = abs(lst[k][1])
    k += 1
    r += 1
    #print(dif_1, dif_2)

    #while dif_1 > 0.00001 or dif_2 > 0.00001:
     #   root(begin, end, r, f_x, k)

root(b,e,r,f_x)

