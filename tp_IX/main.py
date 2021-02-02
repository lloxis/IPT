# exo 1
def nb_chiffres(n):
    """
    Calcul le nombre de chiffres d'un nombre
    :param n:
    :return:
    """
    x = n
    compteur = 0
    while x > 0:
        x = x //10
        compteur += 1
    return compteur

# exo 2
def chiffres(n):
    """
    Donne la liste des chiffres d'un nombre
    :param n:
    :return:
    """
    x = n
    p = nb_chiffres(n)
    chiffres_list = [0]*p
    for i in range(p):
        chiffres_list[p-i-1] = x%10
        x = x //10
    return chiffres_list

# exo 3
def nombre(liste):
    """
    Transforme une liste de chiffres en nombres
    :param liste:
    :return:
    """
    p = len(liste)
    n = 0
    for i in range(p):
        n = 10*n + liste[i]
    return n

def retournement(n):
    """
    Renvoie le nombre retourné
    :param n:
    :return:
    """
    return nombre(chiffres(n)[::-1])

# exo 4
def test(n):
    """
    Renvoie un boolean si n est un palindrome ou non (si n est égal à lui même retourné)
    :param n:
    :return:
    """
    return retournement(n) == n

# exo 5
def suite(u0, n):
    u = u0
    for i in range(n):
        u = u + retournement(u)
    return u

# exo 6
def test_lychrel(n):
    """
    Renvoie un boolean si n est un nombre de lychrel ou non
    :param n:
    :return:
    """
    for i in range(25):
        if test(suite(n, i)):
            return False
    return True

def count_lychrel(n):
    """
    Renvoie le nombre de nombres de lychrel en 0 et n (n non inclus)
    :param n:
    :return:
    """
    compteur = 0
    for i in range(n):
        if test_lychrel(i):
            compteur += 1
    return compteur

# exo 7
def non_palindrome(n):
    """
    Renvoie le premier entier a tel que la suite u est un palindrome qu'à partir de u_n
    :param n:
    :return:
    """
    a = 0
    while True:
        for i in range(n):
            if test(suite(a, i)):
                a += 1
                continue
        return a
