import matplotlib.pyplot as plt

nom = "moto.txt"
fichier = open(nom, "r")
listeBrute = fichier.readlines()
fichier.close()

def traduction(ch):
    ch = ch[:-1]
    return_list = ch.split('\t')
    for i in range(len(return_list)):
        return_list[i] = float(return_list[i])
    return return_list

for i in range(len(listeBrute)):
    listeBrute[i] = traduction(listeBrute[i])

print(listeBrute)

def extraire(k, liste):
    return_list = []
    for i in range(len(liste)):
        return_list.append(liste[i][k-1])
    return return_list

tempsBrut = extraire(1, listeBrute)
accBrute = extraire(3, listeBrute)

## TOUT AFFICHER
plt.subplot(3, 1, 1)
plt.plot(extraire(2, listeBrute))
plt.subplot(3, 1, 2)
plt.plot(accBrute)
plt.subplot(3, 1, 3)
plt.plot(extraire(4, listeBrute))

def rechZero(liste, ecart):
    for i in range(len(liste)):
        if abs(liste[i] - liste[0]) >= ecart:
            return i
    return len(liste)  # si pas e zero

iO = rechZero(accBrute, 1e-2) -1
Delta_t = 0.005

temps = []
for i in range(len(tempsBrut)-iO):
    temps.append(i*Delta_t)

# AFFICHER A PARTIR DU NOUVEAU ZERO
# plt.subplot(4, 1, 4)
# plt.plot(accBrute[iO:])
# plt.show()

def moy(liste):
    moyenne = 0
    n = len(liste)
    for i in range(n):
        moyenne += liste[i]
    return moyenne / n

Vg = moy(accBrute[:iO])
print(Vg)