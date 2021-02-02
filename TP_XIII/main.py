
# exo 1
def degre(P):
    taille = len(P)
    if taille == 0:
        return -1

    coef = 0
    i = 0
    while coef==0:
        if taille-i-1 < 0:
            return -1
        coef = P[taille-i-1]
        i += 1

    return taille-i

# exo 2
def reduire(P):
    return P[:degre(P)+1]

# exo 3
def derive(P):
    P_reduit = reduire(P)
    poly_derive = []
    for i in range(1, len(P_reduit)):
        poly_derive.append(P_reduit[i]*i)
    return poly_derive

# exo 4
def calculNaif(x, P):
    resultat = 0
    i = 0
    for coef in reduire(P):
        resultat += coef*x**i
        i += 1
    return resultat

# exo 6
def horner(x, P):
    P_reduit = reduire(P)
    taille = len(P_reduit)
    if taille == 0:
        return 0
    resultat = 0
    for i in range(1, taille+1):
        resultat = resultat*x + P_reduit[-i]
    return resultat

# exo 7
def somme(P, Q):
    P_reduit = reduire(P)
    Q_reduit = reduire(Q)
    taille_P = len(P_reduit)
    taille_Q = len(Q_reduit)
    resultat = []
    for i in range(max(taille_P, taille_Q)):
        if i >= taille_Q:
            resultat.append(P_reduit[i])
        elif i >= taille_P:
            resultat.append(Q_reduit[i])
        else:
            resultat.append(P_reduit[i]+Q_reduit[i])
    return reduire(resultat)

# exo 8
def produitMonome(P, a, k):
    P_reduit = reduire(P)
    resultat = [0]*k
    for i in range(len(P_reduit)):
        resultat.append(P_reduit[i]*a)
    return resultat

# exo 9
def produitP(P1, P2):
    P1_reduit = reduire(P1)
    P2_reduit = reduire(P2)
    min_len = min(len(P1_reduit), len(P2_reduit))
    if min_len == len(P1_reduit):
        plus_petit_poly = P1
        plus_grand_poly = P2
    else:
        plus_petit_poly = P2
        plus_grand_poly = P1
    resultat = produitMonome(plus_grand_poly, plus_petit_poly[0], 0)
    for i in range(1, min_len):
        resultat = somme(resultat, produitMonome(resultat, plus_petit_poly[i], i))
    return resultat