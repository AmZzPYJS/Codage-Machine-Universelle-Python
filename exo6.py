# Question 6 — Machines de Turing pour les trois fonctions demandées
# - Comparaison d'entiers x#y : s'arrête si x < y, boucle sinon
# - Recherche dans une liste x#w1#w2#... : s'arrête si x = wi, boucle sinon
# - Multiplication unaire 1^n # 1^m : produit 1^(n*m) sur le ruban de sortie

from exo2 import charger_mt
from exo4 import simuler_machine, extraire_resultat
from exo5 import afficher_toutes_les_configurations


def tester_machine(nom_fichier, entree, max_etapes=5000, afficher=False):
    mt = charger_mt(nom_fichier)
    print(f"Machine : {mt.nom}  |  Entrée : '{entree}'  |  Rubans : {mt.nb_rubans}")
    if afficher:
        resultat = afficher_toutes_les_configurations(mt, entree, max_etapes)
    else:
        resultat = simuler_machine(mt, entree, max_etapes)
    print(f"État final : {resultat.etat}")
    for i, ruban in enumerate(resultat.rubans):
        print(f"  Ruban {i+1} : {''.join(ruban).rstrip('_') or '_'}")
    return resultat


if __name__ == "__main__":
    print("=" * 50)
    print("Comparaison d'entiers (x < y → arrêt)")
    print("=" * 50)
    tester_machine("machines/q6_compare.tm", "10#11", 500)
    print()
    tester_machine("machines/q6_compare.tm", "11#10", 200)

    print("\n" + "=" * 50)
    print("Recherche dans une liste")
    print("=" * 50)
    tester_machine("machines/q6_search.tm", "10#01#10#111", 2000)
    print()
    tester_machine("machines/q6_search.tm", "11#01#10#00", 500)

    print("\n" + "=" * 50)
    print("Multiplication unaire (1^n # 1^m → 1^(n*m))")
    print("=" * 50)
    tester_machine("machines/q6_unary_mul.tm", "11#111", 5000)
