from math import *

# exo 1
def diviseurs(n):
    return_list = [1]
    for i in range(2, int(n/2)):
        if n%i == 0:
            return_list.append(i)
    return_list.append(n)
    return return_list

# exo 3
def premier(n):
    diviseurs_list = diviseurs(n)
    for i in range(2, int(sqrt(n))):
        if i in diviseurs_list:
            return False
    return True

# def crible(n):
#     nombres_premiers = [False]*n
#
#     i = 0
#     plus_grand = n
#     for i in range(n-1, 0, -1):
#         if not nombres_premiers[i]:
#             plus_grand = i+1
#     while (i+1)**2 <= plus_grand:
#         while nombres_premiers[i]:
#             i+= 1
#         if not premier(i+1):
#             nombres_premiers[i] = True
#
#         a = 2
#         while (i+1)*a <= n-1:
#             nombres_premiers[(i+1)*a] = True
#             a += 1
#
#         i += 1
#
#     return_list = []
#     for i in range(n):
#         if not nombres_premiers[i]:
#             return_list.append(i)
#     return return_list
