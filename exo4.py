from exo2 import creer_configuration_initiale
from exo3 import un_pas_de_calcul


def simuler_machine(mt, mot, max_etapes=10000):
    config = creer_configuration_initiale(mt, mot)
    compteur = 0

    while True:
        if mt.est_final(config.etat):
            print("Machine arrêtée dans un état final.")
            return config

        if compteur >= max_etapes:
            print("Limite d'étapes atteinte.")
            return config

        nouvelle_config = un_pas_de_calcul(mt, config)

        if nouvelle_config is None:
            print("Machine bloquée.")
            return config

        config = nouvelle_config
        compteur += 1


if __name__ == "__main__":
    from exo2 import charger_mt

    mt = charger_mt("machines/q6_compare.tm")
    resultat = simuler_machine(mt, "10#11", 1000)
    print("État final :", resultat.etat)
    print("Rubans :", resultat.rubans)
    print("Têtes :", resultat.tetes)
