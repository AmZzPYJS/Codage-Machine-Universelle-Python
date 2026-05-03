# Question 8 — Codage binaire de <M>
# On encode la chaîne <M> en UTF-8, chaque octet en 8 bits
# L'interprétation entière est le numéro de Gödel de la machine

from exo7 import coder_machine


def texte_vers_binaire(texte):
    return "".join(format(octet, "08b") for octet in texte.encode("utf-8"))


def binaire_vers_entier(chaine_binaire):
    return int(chaine_binaire, 2) if chaine_binaire else 0


def afficher_codages(nom_fichier):
    codage = coder_machine(nom_fichier)
    codage_binaire = texte_vers_binaire(codage)
    entier = binaire_vers_entier(codage_binaire)
    print("Codage textuel <M> :")
    print(codage)
    print(f"\nLongueur du codage binaire : {len(codage_binaire)} bits")
    print("Codage binaire (50 premiers bits) :")
    print(codage_binaire[:50] + ("..." if len(codage_binaire) > 50 else ""))
    print("\nInterprétation entière :")
    print(entier)


if __name__ == "__main__":
    import os
    if os.path.exists("machines/swap01.tm"):
        afficher_codages("machines/swap01.tm")