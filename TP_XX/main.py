import matplotlib.pyplot as plt
import scipy.optimize

def Newton(f, f_prime, a, epsilon):
    """ Entr é es : deux fonctions r é elles , 2 r é els
    Requis : f est C1 sur un intervalle contenant a
    f_prime est la d é riv é e de f
    epsilon > 0
    Sortie : c appartenant à [ a ; b ] tel qu ’ il existe un
    zero c ’ de f avec | c - c ’| de l ’ ordre de
    epsilon """
    x = a
    ecart = 1 + epsilon
    while ecart >= epsilon:
        x_old = x
        x = x - f(x) / f_prime(x)
        ecart = abs(x - x_old)
    return x


def suite_Newton(f, f_prime, x0, n):
    """ Entr é es : deux fonctions r é elles , 2 r é els
    Requis : f est C1 sur un intervalle contenant a
    f_prime est la d é riv é e de f
    epsilon > 0
    Sortie : c appartenant à [ a ; b ] tel qu ’ il existe un
    zero c ’ de f avec | c - c ’| de l ’ ordre de
    epsilon """
    liste_sortie = []
    x = x0
    for i in range(n + 1):
        x = x - f(x) / f_prime(x)
        liste_sortie.append(x)
    return liste_sortie


# exo2
def P(x):
    return x ** 4 + x ** 3 - 23 * x ** 2 + 3 * x + 90


def dP(x):
    return 4 * x ** 3 + 3 * x ** 2 - 46 * x + 3


# exo 3
# valeurs_x0 = [-10, -8, -6, -4, -2, 0, 2, 4]
#
# for valeur in valeurs_x0:
#     plt.plot(suite_Newton(P, dP, valeur, 10), label=str(valeur))
#
# plt.legend()
# plt.show()

# exo4
def suite(a, b, n):
    liste_sortie = []
    pas = (b - a) / (n - 1)
    for i in range(n):
        liste_sortie.append(a + i * pas)
    return liste_sortie


# exo 5
# X = suite(-5, 2, 100000)
#
# Y=[]
# for i in range(100000):
#     Y.append(Newton(P, dP, X[i], 0.00001))
#
# plt.plot(X, Y)
# plt.show()

# exo 6
def secante(f, a, b, epsilon):
    x_old = a
    x = b
    ecart = 1 + epsilon
    while ecart >= epsilon:
        x_save = x
        x = x - f(x) * (x - x_old) / (f(x) - f(x_old))
        x_old = x_save
        ecart = abs(x - x_old)
    return x


# exo 7
def der(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)


# exo 8
def Newton1(f, a, epsilon):
    h = epsilon / 10
    x = a
    ecart = 1 + epsilon
    while ecart >= epsilon:
        x_old = x
        x = x - f(x) / der(f, x, h)
        ecart = abs(x - x_old)
    return x

print(Newton1(P, -1, 0.1))

#exo 9
def f_a(x, a):
    return a**x-x**2-2

print(scipy.optimize.fsolve(f_a, 2, args=(4)))