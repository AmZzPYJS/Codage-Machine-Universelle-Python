from exo2 import charger_mt, creer_configuration_initiale
from exo3 import un_pas_de_calcul


def simuler_machine(mt, mot):
    config = creer_configuration_initiale(mt, mot)

    print("Départ :", config.tete ,",", config.ruban ,",", config.etat)

    numero_etape = 0

    while config.etat != mt.etat_final:
        nouvelle_config = un_pas_de_calcul(mt, config)

        if nouvelle_config is None:
            print("Aucune transition possible")
            return None

        numero_etape = numero_etape + 1
        config = nouvelle_config

        print("Étape", numero_etape ,":", config.tete ,",", config.ruban ,":", config.etat)

    print("Configuration finale : (", config.tete ,",", config.ruban ,",", config.etat)
    return config


if __name__ == "__main__":
    mt = charger_mt("machine.txt")
    resultat = simuler_machine(mt, "101")