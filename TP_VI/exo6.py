def tout_positif(liste):
    for i in liste:
        if i < 0:
            return False
    return True

def tout_negatif(liste):
    for i in liste:
        if i > 0:
            return False
    return True