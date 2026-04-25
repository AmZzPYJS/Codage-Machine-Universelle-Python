# lancer le code en une ligne de commande pour répondre à chaque question

import sys

from exo2 import charger_mt, creer_configuration_initiale
from exo3 import un_pas_de_calcul
from exo4 import simuler_machine
from exo5 import afficher_toutes_les_configurations
from exo6 import tester_machine
from exo7 import coder_machine
from exo8 import afficher_codages


def aide():
    print("Utilisation :")
    print("python main.py q2 fichier.tm mot")
    print("python main.py q3 fichier.tm mot")
    print("python main.py q4 fichier.tm mot")
    print("python main.py q5 fichier.tm mot")
    print("python main.py q6_compare")
    print("python main.py q6_search")
    print("python main.py q6_mul")
    print("python main.py q7 fichier.tm")
    print("python main.py q8 fichier.tm")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        aide()
        sys.exit(0)

    commande = sys.argv[1]

    if commande == "q2":
        fichier = sys.argv[2]
        mot = sys.argv[3]
        mt = charger_mt(fichier)
        config = creer_configuration_initiale(mt, mot)
        print("Machine :", mt.nom)
        print("État initial :", config.etat)
        print("Rubans :", config.rubans)
        print("Têtes :", config.tetes)

    elif commande == "q3":
        fichier = sys.argv[2]
        mot = sys.argv[3]
        mt = charger_mt(fichier)
        config = creer_configuration_initiale(mt, mot)
        nouvelle_config = un_pas_de_calcul(mt, config)
        if nouvelle_config is None:
            print("Aucune transition possible.")
        else:
            print("Après un pas :")
            print(nouvelle_config.etat, nouvelle_config.rubans, nouvelle_config.tetes)

    elif commande == "q4":
        fichier = sys.argv[2]
        mot = sys.argv[3]
        mt = charger_mt(fichier)
        resultat = simuler_machine(mt, mot)
        print(resultat.etat, resultat.rubans, resultat.tetes)

    elif commande == "q5":
        fichier = sys.argv[2]
        mot = sys.argv[3]
        mt = charger_mt(fichier)
        afficher_toutes_les_configurations(mt, mot)

    elif commande == "q6_compare":
        tester_machine("machines/q6_compare.tm", "10#11", 500, False)

    elif commande == "q6_search":
        tester_machine("machines/q6_search.tm", "10#01#10#111", 1000, False)

    elif commande == "q6_mul":
        tester_machine("machines/q6_unary_mul.tm", "11#111", 5000, False)

    elif commande == "q7":
        fichier = sys.argv[2]
        print(coder_machine(fichier))

    elif commande == "q8":
        fichier = sys.argv[2]
        afficher_codages(fichier)

    else:
        aide()

# Q9 — Machine Universelle
if len(sys.argv) >= 2 and sys.argv[1] == "q9":
    if len(sys.argv) < 3:
        print("Usage: python main.py q9 <codage_M>#<mot>")
        print("Exemple: python main.py q9 machines/swap01.tm 010")
    else:
        from exo7 import coder_machine
        from exo9 import machine_universelle
        codage = coder_machine(sys.argv[2])
        mot = sys.argv[3] if len(sys.argv) > 3 else ""
        entree = f"{codage}#{mot}"
        accepte, ruban, etapes = machine_universelle(entree, verbose=True)

# Q10 — Machine Universelle Bornée
elif len(sys.argv) >= 2 and sys.argv[1] == "q10":
    if len(sys.argv) < 5:
        print("Usage: python main.py q10 <fichier.tm> <mot> <n>")
    else:
        from exo7 import coder_machine
        from exo10 import machine_universelle_bornee
        codage = coder_machine(sys.argv[2])
        mot = sys.argv[3]
        n = sys.argv[4]
        entree = f"{codage}#{mot}#{n}"
        accepte, ruban, etapes, raison = machine_universelle_bornee(entree, verbose=True)
        print(f"\nRaison d'arrêt : {raison} | Étapes : {etapes}")

# Q11 — Preuves
elif len(sys.argv) >= 2 and sys.argv[1] == "q11":
    from exo11 import *
    import exo11
    exec(open("exo11.py").read().split("if __name__")[1].split('"""')[0])
