from exo1 import Configuration
from exo2 import charger_mt, creer_configuration_initiale


def un_pas_de_calcul(mt, config):
    etat_courant = config.etat
    position_tete = config.tete
    ruban = config.ruban

    if position_tete >= len(ruban):
        ruban.append("_")

    if position_tete < 0:
        ruban.insert(0, "_")
        position_tete = 0

    symbole_lu = ruban[position_tete]

    if (etat_courant, symbole_lu) not in mt.transitions:
        return None

    nouvel_etat, symbole_ecrit, mouvement = mt.transitions[(etat_courant, symbole_lu)]

    ruban[position_tete] = symbole_ecrit

    if mouvement == "R":
        position_tete += 1
    elif mouvement == "L":
        position_tete -= 1

    if position_tete >= len(ruban):
        ruban.append("_")

    if position_tete < 0:
        ruban.insert(0, "_")
        position_tete = 0

    return Configuration(
        etat=nouvel_etat,
        ruban=ruban,
        tete=position_tete
    )


if __name__ == "__main__":
    mt = charger_mt("machine.txt")
    config = creer_configuration_initiale(mt, "101")
    print("Avant : (", config.tete,",", config.ruban,",", config.etat ,")")

    nouvelle_config = un_pas_de_calcul(mt, config)

    if nouvelle_config is None:
        print("Aucune transition = Configuration rejetée")
    else:
        print("Après : (", nouvelle_config.tete,",", nouvelle_config.ruban,",", nouvelle_config.etat,")")