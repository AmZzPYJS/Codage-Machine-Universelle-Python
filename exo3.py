from exo1 import Configuration
from exo2 import charger_mt, creer_configuration_initiale


def lire_symbole(config, numero_ruban):
    position = config.tetes[numero_ruban]
    ruban = config.rubans[numero_ruban]

    if position < 0:
        return "_"
    if position >= len(ruban):
        return "_"
    return ruban[position]


def ecrire_symbole(config, numero_ruban, symbole):
    position = config.tetes[numero_ruban]
    ruban = config.rubans[numero_ruban]

    if position < 0:
        while position < 0:
            ruban.insert(0, "_")
            config.tetes[numero_ruban] += 1
            position += 1

    while position >= len(ruban):
        ruban.append("_")

    ruban[position] = symbole


def deplacer_tete(config, numero_ruban, mouvement):
    if mouvement == ">":
        config.tetes[numero_ruban] += 1
    elif mouvement == "<":
        config.tetes[numero_ruban] -= 1
    elif mouvement == "-":
        pass
    else:
        raise ValueError("Mouvement inconnu : " + mouvement)

    # si on dépasse à gauche, on rajoute un blanc
    if config.tetes[numero_ruban] < 0:
        config.rubans[numero_ruban].insert(0, "_")
        config.tetes[numero_ruban] = 0

    # si on dépasse à droite, on rajoute un blanc
    if config.tetes[numero_ruban] >= len(config.rubans[numero_ruban]):
        config.rubans[numero_ruban].append("_")


def un_pas_de_calcul(mt, config):
    symboles_lus = []

    for i in range(mt.nb_rubans):
        symboles_lus.append(lire_symbole(config, i))

    symboles_lus = tuple(symboles_lus)
    cle = (config.etat, symboles_lus)

    if cle not in mt.transitions:
        return None

    nouvel_etat, symboles_ecrits, mouvements = mt.transitions[cle]

    nouvelle_config = config.copier()
    nouvelle_config.etat = nouvel_etat

    for i in range(mt.nb_rubans):
        ecrire_symbole(nouvelle_config, i, symboles_ecrits[i])

    for i in range(mt.nb_rubans):
        deplacer_tete(nouvelle_config, i, mouvements[i])

    return nouvelle_config


if __name__ == "__main__":
    mt = charger_mt("machines/q6_compare.tm")
    config = creer_configuration_initiale(mt, "10#11")

    print("Avant :")
    print(config.etat, config.rubans, config.tetes)

    nouvelle_config = un_pas_de_calcul(mt, config)

    if nouvelle_config is None:
        print("Aucune transition possible.")
    else:
        print("Après :")
        print(nouvelle_config.etat, nouvelle_config.rubans, nouvelle_config.tetes)
