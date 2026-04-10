from exo2 import charger_mt
from exo4 import simuler_machine
from exo5 import afficher_toutes_les_configurations


def tester_machine(nom_fichier, entree, max_etapes=5000, afficher=False):
    mt = charger_mt(nom_fichier)

    if afficher:
        resultat = afficher_toutes_les_configurations(mt, entree, max_etapes)
    else:
        resultat = simuler_machine(mt, entree, max_etapes)

    print("Résultat final :")
    print("État :", resultat.etat)
    print("Rubans :", resultat.rubans)
    print("Têtes :", resultat.tetes)
    return resultat


if __name__ == "__main__":
    print("=== Test comparaison ===")
    tester_machine("machines/q6_compare.tm", "10#11", 500, False)

    print("\n=== Test recherche ===")
    tester_machine("machines/q6_search.tm", "10#01#10#111", 2000, False)

    print("\n=== Test multiplication unaire ===")
    tester_machine("machines/q6_unary_mul.tm", "11#111", 5000, False)