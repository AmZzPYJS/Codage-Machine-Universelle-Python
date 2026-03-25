from exo1 import MT, Configuration

def charger_mt(nom_fichier):
    etats = set()
    alphabet_entree = set()
    alphabet_travail = set()
    transitions = {}
    etat_initial = ""
    etat_final = ""

    with open(nom_fichier, "r", encoding="utf-8") as f:
        for ligne in f:
            ligne = ligne.strip()

            if not ligne:
                continue

            if ligne.startswith("etats:"):
                etats = set(ligne.split(":", 1)[1].split(","))

            elif ligne.startswith("alphabet_entree:"):
                alphabet_entree = set(ligne.split(":", 1)[1].split(","))

            elif ligne.startswith("alphabet_travail:"):
                alphabet_travail = set(ligne.split(":", 1)[1].split(","))

            elif ligne.startswith("etat_initial:"):
                etat_initial = ligne.split(":", 1)[1]

            elif ligne.startswith("etat_final:"):
                etat_final = ligne.split(":", 1)[1]

            elif ligne.startswith("transition:"):
                contenu = ligne.split(":", 1)[1].strip()
                gauche, droite = contenu.split("->")

                etat_courant, symbole_lu = gauche.split(",")
                nouvel_etat, symbole_ecrit, mouvement = droite.split(",")

                transitions[(etat_courant.strip(), symbole_lu.strip())] = (
                    nouvel_etat.strip(),
                    symbole_ecrit.strip(),
                    mouvement.strip()
                )

    return MT(
        etats=etats,
        alphabet=alphabet_entree,
        alphabet_de_travail=alphabet_travail,
        transitions=transitions,
        etat_initial=etat_initial.strip(),
        etat_final=etat_final.strip()
    )


def creer_configuration_initiale(mt, mot_entree):
    ruban = list(mot_entree) + ["_"]
    return Configuration(mt.etat_initial, ruban, 0)


if __name__ == "__main__":
    mt = charger_mt("machine.txt")
    config = creer_configuration_initiale(mt, "101")
    print("Suite de configuration : (", config.tete,",",config.ruban,",",config.etat, ")")