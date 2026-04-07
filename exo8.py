from exo7 import coder_machine


def texte_vers_binaire(texte):
    donnees = texte.encode("utf-8")
    resultat = ""

    for octet in donnees:
        resultat += format(octet, "08b")

    return resultat


def binaire_vers_entier(chaine_binaire):
    if chaine_binaire == "":
        return 0
    return int(chaine_binaire, 2)


def afficher_codages(nom_fichier):
    codage = coder_machine(nom_fichier)
    codage_binaire = texte_vers_binaire(codage)
    entier = binaire_vers_entier(codage_binaire)

    print("Codage textuel :")
    print(codage)
    print()

    print("Codage binaire :")
    print(codage_binaire)
    print()

    print("Interprétation entière :")
    print(entier)


if __name__ == "__main__":
    afficher_codages("machines/q6_compare.tm")
