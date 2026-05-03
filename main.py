# Lancer le code en une ligne de commande pour répondre à chaque question

import sys

from exo2 import charger_mt, creer_configuration_initiale
from exo3 import un_pas_de_calcul
from exo4 import simuler_machine
from exo5 import afficher_toutes_les_configurations
from exo6 import tester_machine
from exo7 import coder_machine
from exo8 import afficher_codages
from exo9 import machine_universelle
from exo10 import machine_universelle_bornee


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
    print("python main.py q9 fichier.tm mot")
    print("python main.py q10 fichier.tm mot n")
    print("python main.py q11")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        aide()
        sys.exit(0)

    commande = sys.argv[1]

    if commande == "q2":
        mt = charger_mt(sys.argv[2])
        config = creer_configuration_initiale(mt, sys.argv[3])
        print("Machine :", mt.nom)
        print("État initial :", config.etat)
        print("Rubans :", config.rubans)

    elif commande == "q3":
        mt = charger_mt(sys.argv[2])
        config = creer_configuration_initiale(mt, sys.argv[3])
        nouvelle = un_pas_de_calcul(mt, config)
        if nouvelle is None:
            print("Aucune transition possible.")
        else:
            print(nouvelle.etat, nouvelle.rubans, nouvelle.tetes)

    elif commande == "q4":
        mt = charger_mt(sys.argv[2])
        simuler_machine(mt, sys.argv[3])

    elif commande == "q5":
        mt = charger_mt(sys.argv[2])
        afficher_toutes_les_configurations(mt, sys.argv[3])

    elif commande == "q6_compare":
        tester_machine("machines/q6_compare.tm", "10#11", 500)

    elif commande == "q6_search":
        tester_machine("machines/q6_search.tm", "10#01#10#111", 1000)

    elif commande == "q6_mul":
        tester_machine("machines/q6_unary_mul.tm", "11#111", 5000)

    elif commande == "q7":
        print(coder_machine(sys.argv[2]))

    elif commande == "q8":
        afficher_codages(sys.argv[2])

    elif commande == "q9":
        codage = coder_machine(sys.argv[2])
        mot = sys.argv[3] if len(sys.argv) > 3 else ""
        machine_universelle(codage + "#" + mot, verbose=True)

    elif commande == "q10":
        if len(sys.argv) < 5:
            print("Usage: python main.py q10 fichier.tm mot n")
        else:
            codage = coder_machine(sys.argv[2])
            entree = f"{codage}#{sys.argv[3]}#{sys.argv[4]}"
            _, _, etapes, raison = machine_universelle_bornee(entree, verbose=True)
            print(f"Raison d'arrêt : {raison} | Étapes : {etapes}")

    elif commande == "q11":
        print("Question 11 — Décidabilité des langages L1, L2, L3")
        print("Voir le fichier exo11_preuves.pdf pour les preuves formelles.")

    else:
        aide()
