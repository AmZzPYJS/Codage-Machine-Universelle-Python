from exo2 import charger_mt, creer_configuration_initiale
from exo3 import un_pas_de_calcul


def afficher_configuration(config):
    print("État :", config.etat)
    for i in range(len(config.rubans)):
        print("Ruban", i + 1, ":", "".join(config.rubans[i]))
        print("         ", " " * config.tetes[i] + "^")
    print("-" * 40)


def afficher_toutes_les_configurations(mt, mot, max_etapes=1000):
    config = creer_configuration_initiale(mt, mot)
    compteur = 0

    print("Configuration initiale :")
    afficher_configuration(config)

    while not mt.est_final(config.etat):
        if compteur >= max_etapes:
            print("Limite d'étapes atteinte.")
            return config

        nouvelle_config = un_pas_de_calcul(mt, config)

        if nouvelle_config is None:
            print("Machine bloquée.")
            return config

        config = nouvelle_config
        compteur += 1

        print("Étape", compteur)
        afficher_configuration(config)

    print("Machine arrêtée dans un état final.")
    return config


if __name__ == "__main__":
    mt = charger_mt("machines/q6_compare.tm")
    afficher_toutes_les_configurations(mt, "10#11", 200)
