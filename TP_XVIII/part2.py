from math import *
import matplotlib.pyplot as plt

def f1(t):
    return 4 / (1+t**2)

F1 = []
T = []
for k in range(0, 1001):
    t_k = k*10**(-3)
    T.append(t_k)
    F1.append(f1(t_k))

plt.plot(T, F1)
plt.show()

def integrale_rg(T, Y):
    pas = T[1] - T[0]
    n = int((T[-1] - T[0])/pas)
    s = 0
    for k in range(n-1):
        s += Y[k]
    return s*pas

print(integrale_rg(T, F1))