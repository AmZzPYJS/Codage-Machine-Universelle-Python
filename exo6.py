# Question 6 — Machines de Turing pour les trois fonctions demandées

from exo2 import charger_mt
from exo4 import simuler_machine, extraire_resultat
from exo5 import afficher_toutes_les_configurations


def tester_machine(nom_fichier, entree, max_etapes=5000, afficher=False):
    """
    Charge une machine depuis nom_fichier et la simule sur entree.
    Si afficher=True, affiche toutes les configurations étape par étape.
    Retourne la configuration finale.
    """
    mt = charger_mt(nom_fichier)
    print(f"Machine : {mt.nom}  |  Entrée : '{entree}'  |  Rubans : {mt.nb_rubans}")

    if afficher:
        resultat = afficher_toutes_les_configurations(mt, entree, max_etapes)
    else:
        resultat = simuler_machine(mt, entree, max_etapes)

    print(f"État final : {resultat.etat}")
    for i, ruban in enumerate(resultat.rubans):
        contenu = "".join(ruban).rstrip("_") or "_"
        print(f"  Ruban {i+1} : {contenu}")
    return resultat


if __name__ == "__main__":
    print("=" * 50)
    print("Test 1 — Comparaison d'entiers (x < y → arrêt)")
    print("=" * 50)
    print("Cas 10 < 11 (binaire) → doit s'arrêter :")
    tester_machine("machines/q6_compare.tm", "10#11", 500)
    print()
    print("Cas 11 >= 10 → doit boucler (arrêt forcé à 200 étapes) :")
    tester_machine("machines/q6_compare.tm", "11#10", 200)

    print()
    print("=" * 50)
    print("Test 2 — Recherche dans une liste")
    print("=" * 50)
    print("'10' présent dans [01, 10, 111] → doit s'arrêter :")
    tester_machine("machines/q6_search.tm", "10#01#10#111", 2000)
    print()
    print("'11' absent de [01, 10, 00] → doit boucler (arrêt forcé) :")
    tester_machine("machines/q6_search.tm", "11#01#10#00", 500)

    print()
    print("=" * 50)
    print("Test 3 — Multiplication unaire (1^n # 1^m → 1^(n*m))")
    print("=" * 50)
    print("11 # 111 = 1^2 * 1^3 → résultat attendu : 111111 (1^6) :")
    tester_machine("machines/q6_unary_mul.tm", "11#111", 5000)
