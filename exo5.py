# Question 5 — Affichage des configurations au fil de l'exécution

from exo2 import charger_mt, creer_configuration_initiale
from exo3 import un_pas_de_calcul


def afficher_configuration(config, etape=None):
    entete = f"Étape {etape}" if etape is not None else "Configuration initiale"
    print(f"{entete}  |  État : {config.etat}")
    for i, ruban in enumerate(config.rubans):
        label = f"Ruban {i+1} :"
        contenu = "".join(ruban)
        padding = " " * (len(label) + 1 + config.tetes[i])
        print(f"  {label} {contenu}")
        print(f"  {padding}^")
    print("-" * 40)


def afficher_toutes_les_configurations(mt, mot, max_etapes=1000):
    config = creer_configuration_initiale(mt, mot)
    afficher_configuration(config)
    compteur = 0

    while not mt.est_final(config.etat):
        if compteur >= max_etapes:
            print(f"Limite de {max_etapes} étapes atteinte.")
            return config
        nouvelle_config = un_pas_de_calcul(mt, config)
        if nouvelle_config is None:
            print(f"Machine bloquée à l'étape {compteur}.")
            return config
        config = nouvelle_config
        compteur += 1
        afficher_configuration(config, etape=compteur)

    print("Machine arrêtée dans un état final.")
    return config


if __name__ == "__main__":
    mt = charger_mt("machines/q6_compare.tm")
    afficher_toutes_les_configurations(mt, "10#11", 200)
