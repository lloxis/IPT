LO = [34, 32, 27, 15, 21, 23, 29, 40, 35, 31, 12, 26, 25, 33]

# exo 2
def minimum(liste):
    n = len(liste)
    a = liste[0]
    for i in range(1, n):
        if liste[i] < a:
            a = liste[i]
    return a

# exo 3
def moyenne(liste):
    return_moyenne = 0
    for i in liste:
        return_moyenne += i
    return return_moyenne / len(liste)

# exo 4
def ecart_type(liste):
    variance = 0
    moy = moyenne(liste)
    for i in liste:
        variance += (i - moy)**2
    variance = variance / len(liste)
    return variance**0.5

# exo 5
def nb_plus(liste, a):
    nombre_indices = 0
    for i in range(len(liste)):
        if liste[i] > a:
            nombre_indices +=1
    return nombre_indices

# exo 6
def ind_moins(liste, a):
    indices_liste = []
    for i in range(len(liste)):
        if liste[i] < a:
            indices_liste.append(i)
    return indices_liste

# exo 7
def moyenne_jour(liste):
    n = len(liste)
    liste_moyenne_jour = []
    for i in range(7):
        liste_moyenne_jour.append(moyenne(liste[i:n:7]))
    return liste_moyenne_jour

# exo 8
def maximum(liste):
    """
    Renvoie la valeur du maximum puis l'indice du maxium
    """
    n = len(liste)
    maxi = liste[0]
    indice_max = 0
    for i in range(1, n):
        if liste[i] > maxi:
            maxi = liste[i]
            indice_max = i
    return maxi, indice_max

jours = ["dimanche", "lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi"]
def jour_max(liste):
    # indice_max est l'indice du jour qui a la plus grande moyenne de réservation
    indice_max = maximum(moyenne_jour(liste))[1]
    return jours[indice_max]

# exo 9
def totaux_semaine(liste):
    liste_totaux_semaines = []
    total_semaine = 0
    for i in range(len(liste)):
        total_semaine += liste[i]
        if i%7 == 6:
            liste_totaux_semaines.append(total_semaine)
            total_semaine = 0
    return liste_totaux_semaines

EO = [2, 15, 1, -2, 6, 4, 3, 0, 7, 2, -2, 1, 1]

# exo 10
def nb_retards(liste, seuil):
    nb_retards_total = 0
    for i in liste:
        if i > seuil:
            nb_retards_total +=1
    return nb_retards_total

# exo 11
# !! Ici je propose 2 fonction différentes
# La premiere calcul la vraie moyenne des retards, qui n'est pas la valeur donnée dans l'énoncé
def moy_retards_1(liste):
    retards_liste = []
    for i in liste:
        if i > 0:
            retards_liste.append(i)
    return moyenne(retards_liste)

# la seconde calcul la moyenne en fesant la somme des termes positifs divisée par la longueure de la liste
# Ce n'est pas la vraie moyenne des retards car on divise par la longueure de la liste et non le nombre de termes positif
# ici on obtient le même résultat que l'énoncé
def moy_retards_2(liste):
    moy = 0
    for i in liste:
        if i > 0:
            moy += i
    return moy / len(liste)

# exo 12
def pointage(liste, seuil):
    retards_indices_liste = []
    for i in range(len(liste)):
        if liste[i] > seuil:
            retards_indices_liste.append(i)
    return retards_indices_liste

# exo 13
def pointage1(liste, seuil):
    retards_indices_liste = []
    for i in range(len(liste)):
        if liste[i] > seuil:
            retards_indices_liste.append(i)
    return [-1] + retards_indices_liste + [len(liste)]

# exo 14
def plage_max(liste, seuil):
    # si toutrs les valeurs sont supérieures au seuil on renvoie 0
    for i in range(len(liste)):
        if liste[i] < seuil:
            break
        if i >= len(liste)-1:
            return 0

    max_k = 0
    k = 0
    for i in range(len(liste)):
        if liste[i] <= seuil:
            k += 1
        else:
            k = 0
        if k > max_k:
            max_k = k
    return max_k

# exo 15
def bornes_plage_max(liste, seuil):
    # si toutrs les valeurs sont supérieures au seuil on renvoie 0, -1
    for i in range(len(liste)):
        if liste[i] < seuil:
            break
        if i >= len(liste) - 1:
            return 0, -1

    max_k = 0
    b = 0
    k = 0
    for i in range(len(liste)):
        if liste[i] <= seuil:
            k += 1
        else:
            k = 0
        if k > max_k:
            max_k = k
            b = i
    return b - max_k + 1, b

# exo 16
arriveesO = [495, 562, 740, 841, 920, 1264]
departO = [624, 803, 950, 1047, 1133, 1320]
def nb_quais(arrivees, departs):
    nb_quais_neccessaires = 0
    max_nb_quais_neccessaires = 0
    for i in range(0, 1441):  # car il y a 1440 minutes dans une journée
        if i in arrivees:
            nb_quais_neccessaires +=1
        elif i in departs:
            nb_quais_neccessaires -= 1
        if nb_quais_neccessaires > max_nb_quais_neccessaires:
            max_nb_quais_neccessaires = nb_quais_neccessaires
    return max_nb_quais_neccessaires
