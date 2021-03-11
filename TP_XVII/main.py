from math import *
import matplotlib.pyplot as plt
import random as rd

# exo 1
def moyenne(liste):
    n = len(liste)
    resultat = 0
    for valeur in liste:
        resultat += valeur
    return resultat/n

def ecrat_type(liste):
    n = len(liste)
    moy = moyenne(liste)
    variance_liste = []
    for i in range(n):
        variance_liste.append((liste[i]-moy)**2)
    variance = moyenne(variance_liste)
    return sqrt(variance)

def maximum(liste):
    n = len(liste)
    if n < 1:
        raise ValueError("La liste ne doit pas être vide !")
    resultat = liste[0]
    for valeur in liste:
        if valeur > resultat:
            resultat = valeur
    return resultat

def minimum(liste):
    n = len(liste)
    if n < 1:
        raise ValueError("La liste ne doit pas être vide !")
    resultat = liste[0]
    for valeur in liste:
        if valeur < resultat:
            resultat = valeur
    return resultat

L0 = [4.3, 5.1, 7.8, 5.4, 4.4, 7.3, 6.8, 6.7, 5.9, 7.1]

def comptage(liste, n):
    mini = minimum(liste)
    maxi = maximum(liste)
    h = 1/n *(maxi-mini)
    histo = [0]*n
    for x in liste:
        k = int((x-mini) / h)
        if k == n:
            k = n-1
        histo[k] += 1
    return histo, h, mini

def histogramme(liste, n):
    valeurs, h, mini = comptage(liste, n)
    centres = [mini + k*h + h/2 for k in range(n)]
    plt.bar(centres, valeurs, width=h)
    plt.show()
    return h

def liste_alea(x0, e, n):
    resultat = []
    for i in range(n):
        resultat.append(rd.random()*2*e + x0-e)
    return resultat

# exo 7
A = liste_alea(12.5, 0.05, 10000)
B = liste_alea(8.3, 0.05, 10000)
X = []
for i in range(10000):
    X.append(A[i]+B[i])
# histogramme(X, 20)

# exo 8
A = liste_alea(12.5, 0.05, 10000)
B = liste_alea(8.32, 0.005, 10000)
X = []
for i in range(10000):
    X.append(A[i]+B[i])
# histogramme(X, 20)

# exo 9
A = liste_alea(12.5, 0.05, 10000)
B = liste_alea(8.3, 0.05, 10000)
C = liste_alea(4.7, 0.05, 10000)
D = liste_alea(13.4, 0.05, 10000)
X = []
for i in range(10000):
    X.append((A[i]+B[i]) / (C[i]+D[i]))
# histogramme(X, 50)

# exo 10
X = []
for i in range(100):
    X.append(liste_alea(12.5, 0.05, 100000))

M = []
for i in range(100000):
    M.append(moyenne([X[k][i] for k in range(100)]))
m = moyenne(M)
ecart = ecrat_type(M)

nb_de_points_courbe = 1000
mini = minimum(M)
maxi = maximum(M)
K = (maxi-mini) * 200
liste_x = [12.48 + (12.52-12.48)/nb_de_points_courbe * k for k in range(nb_de_points_courbe)]
liste_y = [K/(sqrt(2*pi)*ecart) * exp((-(x - m)**2) / (2*ecart**2)) for x in liste_x]
plt.plot(liste_x, liste_y, color='red')
plt.show()
histogramme(M, 50)