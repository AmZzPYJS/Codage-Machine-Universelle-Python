# Question 8 — Codage binaire de <M>
#
# On code la chaîne textuelle produite par la question 7 en UTF-8,
# puis on convertit chaque octet en binaire sur 8 bits (big-endian).
# L'interprétation entière est l'entier naturel correspondant à cette séquence de bits.
#
# Ce choix est justifié car :
# - UTF-8 est un codage universel (gère tous les caractères ASCII + □)
# - La taille du codage reste raisonnable
# - La bijection texte → entier est triviale et réversible

from exo7 import coder_machine


def texte_vers_binaire(texte):
    """Encode la chaîne en UTF-8 puis convertit chaque octet en 8 bits."""
    donnees = texte.encode("utf-8")
    return "".join(format(octet, "08b") for octet in donnees)


def binaire_vers_entier(chaine_binaire):
    """Interprète la chaîne binaire comme un entier naturel."""
    return int(chaine_binaire, 2) if chaine_binaire else 0


def afficher_codages(nom_fichier):
    """Affiche le codage textuel, binaire et l'entier correspondant."""
    codage = coder_machine(nom_fichier)
    codage_binaire = texte_vers_binaire(codage)
    entier = binaire_vers_entier(codage_binaire)

    print("Codage textuel <M> :")
    print(codage)
    print()
    print(f"Longueur du codage binaire : {len(codage_binaire)} bits")
    print("Codage binaire (50 premiers bits) :")
    print(codage_binaire[:50] + ("..." if len(codage_binaire) > 50 else ""))
    print()
    print("Interprétation entière :")
    print(entier)


if __name__ == "__main__":
    # Les 3 machines Q6 sont multi-rubans → erreurs attendues
    for fichier, label in [
        ("machines/q6_compare.tm",    "q6_compare   (2 rubans)"),
        ("machines/q6_search.tm",     "q6_search    (2 rubans)"),
        ("machines/q6_unary_mul.tm",  "q6_unary_mul (3 rubans)"),
    ]:
        print(f"=== {label} ===")
        try:
            afficher_codages(fichier)
        except ValueError as e:
            print(f"[OK] Erreur attendue : {e}")
        print()
