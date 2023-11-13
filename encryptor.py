
def saisir_cle(cle):
    if len(cle) != 5:
        print("La clé doit avoir une longueur de 5 caractères.")
        return False
    if not any(char.isalpha() for char in cle) or not any(char.isdigit() for char in cle):
        print("La clé doit contenir à la fois des lettres et des chiffres.")
        return False
    
    return True

def cryptage(text, cle):
    cryptage_text = ""
    long_cle = len(cle)
    for i, mot in enumerate(text):
        if mot.isalpha():
            depart_alpha = ord('a') if mot.islower() else ord('A')
            key_char = cle[i % long_cle]
            decalage = ord(key_char.lower()) - ord('a')
            cryptage_text += chr((ord(mot) - depart_alpha + decalage) % 26 +depart_alpha)
        else:
            cryptage_text += mot
    return cryptage_text

