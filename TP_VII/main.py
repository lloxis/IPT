from copy import deepcopy
liste1 = [0, 1, 2, 3, 4, 5, 6]

# exo 10
def echanger(liste, index_a, index_b):
    temp_a = liste[index_a]
    liste[index_a] = liste[index_b]
    liste[index_b] = temp_a

# exo 11
def retourner(liste):
    liste_copy = deepcopy(liste)
    for i in range(len(liste)):
        liste[i] = liste_copy[-i-1]

# exo 12
def decaler1(liste):
    liste_copy = deepcopy(liste)
    for i in range(len(liste)):
        liste[i] = liste_copy[i-1]

# exo 12 - autre méthode
def decaler1_bis(liste):
    for i in range(len(liste)-1, 0, -1):
        echanger(liste, i, i-1)

def decaler(k, liste):
    liste_copy = deepcopy(liste)
    for i in range(len(liste)):
        liste[i] = liste_copy[i - k]