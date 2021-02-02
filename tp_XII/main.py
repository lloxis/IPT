import random as rd

ch0 = "GATGCATTAGTAAGGGGTAGA"

# exo 1
def ADN(n):
    chaine = ""
    for i in range(n):
        chaine += rd.choice('ACGT')
    return chaine

# exo 2
def nb_lettres(chaine, lettre):
    compteur = 0
    for char in chaine:
        if char == lettre:
            compteur += 1
    return compteur

# exo 3
def composition(chaine):
    char_possible = ['A', 'C', 'G', 'T', 'B']
    compteurs = [0]*len(char_possible)
    for char in chaine:
        index = char_possible.index(char)
        if index >= 0:
            compteurs[index] += 1
    for i in range(len(char_possible)):
        freq = compteurs[i]
        print(freq, 'fois', char_possible[i], ', soit', freq*100/len(chaine), '%')

# exo 4
def renserse(chaine):
    chaine_reverse = ''
    for i in range(len(chaine)-1, -1, -1):
        chaine_reverse += chaine[i]
    return chaine_reverse

# exo 5
def changement(chaine, k, car):
    return chaine[:k] + car + chaine[k+1:]

# exo 6
def mutation(chaine):
    random_index = rd.randint(0, len(chaine)-1)
    char_remplace = ['A', 'C', 'G', 'T']
    char_remplace.remove(chaine[random_index])
    return changement(chaine, random_index, rd.choice(char_remplace))

# exo 7
def mutations(chaine, T):
    chaine_mutee = chaine
    nb_mutations = int(1.5e-2*len(chaine)*T)
    for i in range(nb_mutations):
        chaine_mutee = mutation(chaine_mutee)
    return chaine_mutee

# exo 8
def mutationK(chaine):
    random_index = rd.randint(0, len(chaine)-1)
    ancien_char = chaine[random_index]
    char_remplace = ''
    random_nb = rd.random()
    if random_nb <= 2/3:
        if ancien_char == 'A':
            char_remplace = 'G'
        if ancien_char == 'G':
            char_remplace = 'A'
        if ancien_char == 'C':
            char_remplace = 'T'
        if ancien_char == 'T':
            char_remplace = 'C'
    else:
        if ancien_char in 'AG':
            char_remplace = rd.choice('CT')
        if ancien_char in 'CT':
            char_remplace = rd.choice('AG')
    return changement(chaine, random_index, char_remplace)

# exo 9
def difference(ch1, ch2):
    return_string = ''
    for i in range(len(ch1)):
        if ch1[i] == ch2[i]:
            return_string += ' '
        else:
            return_string += 'X'
    print(ch1 + '\n' + ch2 + '\n' + return_string)