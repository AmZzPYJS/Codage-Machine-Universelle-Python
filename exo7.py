# Pour la question : Que faudrait-il faire si on veut pouvoir accepter n’importe quel alphabet de travail ?
# Réponse: Il faut utiliser un encodage générique des symboles, par exemple en considérant les symboles comme des chaînes de 
# caractères et en les encodant ensuite en UTF-8. Ainsi, le codage fonctionne quel que soit l’alphabet de travail.

def nettoyer_ligne(ligne):
    if "//" in ligne:
        ligne = ligne.split("//")[0]
    return ligne.strip()


def lire_lignes_utiles(nom_fichier):
    lignes_utiles = []

    with open(nom_fichier, "r", encoding="utf-8") as f:
        for ligne in f:
            ligne = nettoyer_ligne(ligne)
            if ligne != "":
                lignes_utiles.append(ligne)

    return lignes_utiles


def coder_machine(nom_fichier):
    lignes_utiles = lire_lignes_utiles(nom_fichier)
    return "|".join(lignes_utiles)


if __name__ == "__main__":
    codage = coder_machine("machines/q6_compare.tm")
    print("Codage textuel :")
    print(codage)
