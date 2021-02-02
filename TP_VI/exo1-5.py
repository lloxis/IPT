import matplotlib.pyplot as plt

T0 = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0,
           1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0,
           2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0,
           3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0]

X0 = [0.00, 0.84, 1.56, 2.18, 2.70, 3.12, 3.45, 3.70, 3.87,
      3.96, 4.00, 3.97, 3.88, 3.75, 3.58, 3.37, 3.13,
      2.87, 2.59, 2.29, 2.00, 1.70, 1.40, 1.12, 0.86,
      0.62, 0.41, 0.24, 0.11, 0.02, 0.00, 0.03, 0.12,
      0.29, 0.54, 0.87, 1.29, 1.81, 2.43, 3.15, 4.00]

Y0 = [1.64, 3.64, 5.71, 6.16, 8.08, 9.31, 9.82, 9.91, 10.8,
      10.6, 11.4, 10.7, 10.8, 10.6, 9.58, 9.43, 8.85,
      8.95, 7.92, 6.66, 6.04, 4.79, 5.24, 4.05, 3.91,
      3.12, 2.82, 1.92, 2.21, 2.03, 1.42, 1.82, 2.45,
      2.18, 2.58, 3.95, 4.85, 6.29, 6.83, 8.61, 10.5]


def moyenne(liste):
    """
    calcul la moyenne de la liste
    :param liste:
    :return:
    """
    resultat = 0
    for i in liste:
        resultat += i
    return resultat / len(liste)


def var(liste):
    """
    calcul la variance de la liste
    :param liste:
    :return:
    """
    moyenne_value = moyenne(liste)
    resultat = 0
    for i in liste:
        resultat += (i - moyenne_value) ** 2
    return resultat / len(liste)


def cov(liste_X, liste_Y):
    """
    calcul la covariance des 2 listes
    les 2 listes doivent être de même longueur
    """
    resultat = 0
    moyenne_liste1 = moyenne(liste_X)
    moyenne_liste2 = moyenne(liste_Y)
    for i in range(len(liste_X)):
        resultat += (liste_X[i] - moyenne_liste1) * (liste_Y[i] - moyenne_liste2)
    return resultat / len(liste_X)


def regression(liste_X, liste_Y):
    a = cov(liste_X, liste_Y) / var(liste_X)
    b = moyenne(liste_Y) - a * moyenne(liste_X)
    return a, b


def afficher_regression(liste_X, liste_Y):
    plt.plot(liste_X, liste_Y, 'o')
    a, b = regression(liste_X, liste_Y)
    # plt.plot([0, liste_X[-1]], [regression(liste_X, liste_Y)[1], liste_X[-1]*regression(liste_X, liste_Y)[0]+regression(liste_X, liste_Y)[1]], linestyle='-')
    plt.axline([0, b], slope=a, color='r')
    plt.show()

def tout_positif(liste):
    for i in liste:
        if i < 0:
            return False
    return True

def existe_positif(liste):
    for i in liste:
        if i > 0:
            return True
    return False

def croissante(liste):
    for i in range(1, len(liste)):
        if liste[i-1] > liste[i]:
            return False
    return True

def minimum(liste2):
    minim = liste2[0]
    for i in range(1, len(liste2)):
        if liste2[i] < minim:
            minim = liste2[i]
    return minim
