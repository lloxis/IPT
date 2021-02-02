from random import randint

# exo 1
def Collatz(a, n):
    u = a
    for i in range(n):
        if u%2 == 0:
            u = u//2
        else:
            u = 3*u+1
    return u

def Collatz_list(a):
    for i in range(longueurCollatz(a)):
        print(Collatz(a, i))

# exo 2
def longueurCollatz(a):
    if a == 0:
        return 0
    n = 0
    while Collatz(a, n) != 1:
        n +=1
    return n

# exo 3 et 4
def hauteurCollatz(a):
    maxi = a
    indice_maxi = 0
    n = 0
    for i in range(longueurCollatz(a)):
        u_n = Collatz(a, n)
        if u_n > maxi:
            maxi = u_n
            indice_maxi = n
        n += 1
    return maxi, indice_maxi

# exo 5
def longueurSeuil(s):
    """

    :param s: longeur seuil
    :return:
    """
    a = 0
    longueur = 0
    while longueur <= s:
        a += 1
        longueur = longueurCollatz(a)
    return a, longueur

# exo 6
def hauteurSeuil(s):
    """
    Trouve la liste de Collatz avec la valeur de a la plus petite telle que la hauteur seuil est dépassée
    :param s: hauteur seuil
    :return: le maxi atteint, l'indice auquel il est attient, la valeur initiale a
    """
    a = 0
    hauteur = (0, 0)
    while hauteur[0] <= s:
        a += 1
        hauteur = hauteurCollatz(a)
    return hauteur[0], a, hauteur[1]

#ex 7
def logEntier(n):
    p = 0
    while 2**p > n or n >= 2**(p+1):
        p +=1
    return p

# exo 9
def trois_fois_de_suite():
    nombre_de_tirages=0
    nombre_de_1 = 0
    while nombre_de_1 < 3:
        tirage = randint(0, 1)
        if tirage == 1:
            nombre_de_1 += 1
        else:
            nombre_de_1 = 0
        nombre_de_tirages += 1
    return nombre_de_tirages