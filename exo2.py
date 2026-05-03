# Question 2 — Chargement d'une machine depuis un fichier .tm
# et création de la configuration initiale

from exo1 import MT, Configuration


def nettoyer_ligne(ligne):
    if "//" in ligne:
        ligne = ligne.split("//")[0]
    return ligne.strip()


def decouper_csv(ligne):
    return [x.strip() for x in ligne.split(",") if x.strip() != ""]


# Lit un fichier .tm et retourne un objet MT
def charger_mt(nom_fichier):
    nom = ""
    etats = set()
    alphabet_entree = set()
    alphabet_travail = set()
    transitions = {}
    etat_initial = ""
    etats_finaux = set()
    nb_rubans = None

    with open(nom_fichier, "r", encoding="utf-8") as f:
        lignes = [nettoyer_ligne(ligne) for ligne in f]
    lignes = [ligne for ligne in lignes if ligne != ""]

    i = 0
    while i < len(lignes):
        ligne = lignes[i]

        if ligne.startswith("name:"):
            nom = ligne.split(":", 1)[1].strip()
            i += 1
            continue

        if ligne.startswith("init:"):
            etat_initial = ligne.split(":", 1)[1].strip()
            etats.add(etat_initial)
            i += 1
            continue

        if ligne.startswith("accept:"):
            partie = ligne.split(":", 1)[1].strip()
            for q in [x.strip() for x in partie.split(",") if x.strip()]:
                etats_finaux.add(q)
                etats.add(q)
            i += 1
            continue

        if "," in ligne:
            if i + 1 >= len(lignes):
                raise ValueError("Transition incomplète dans le fichier.")

            ligne_lecture  = decouper_csv(lignes[i])
            ligne_ecriture = decouper_csv(lignes[i + 1])

            etat_courant  = ligne_lecture[0]
            symboles_lus  = tuple(ligne_lecture[1:])

            if nb_rubans is None:
                nb_rubans = len(symboles_lus)
            if len(symboles_lus) != nb_rubans:
                raise ValueError("Nombre de rubans incohérent dans une transition.")
            if len(ligne_ecriture) != 1 + 2 * nb_rubans:
                raise ValueError("Ligne d'écriture invalide.")

            nouvel_etat    = ligne_ecriture[0]
            symboles_ecrits = tuple(ligne_ecriture[1:1 + nb_rubans])
            mouvements     = tuple(ligne_ecriture[1 + nb_rubans:1 + 2 * nb_rubans])

            transitions[(etat_courant, symboles_lus)] = (nouvel_etat, symboles_ecrits, mouvements)
            etats.add(etat_courant)
            etats.add(nouvel_etat)
            for s in symboles_lus + symboles_ecrits:
                alphabet_travail.add(s)

            i += 2
            continue

        i += 1

    if nb_rubans is None:
        nb_rubans = 1

    alphabet_entree = set(alphabet_travail)
    if "_" in alphabet_entree:
        alphabet_entree.remove("_")

    return MT(nom=nom, etats=etats, alphabet=alphabet_entree,
              alphabet_de_travail=alphabet_travail, transitions=transitions,
              etat_initial=etat_initial, etats_finaux=etats_finaux, nb_rubans=nb_rubans)


def creer_configuration_initiale(mt, mot_entree):
    # Ruban 0 = mot d'entrée + blanc sentinelle, autres rubans = vides
    rubans = []
    for i in range(mt.nb_rubans):
        if i == 0:
            ruban = list(mot_entree) if mot_entree else ["_"]
            if mot_entree:
                ruban.append("_")
        else:
            ruban = ["_"]
        rubans.append(ruban)
    return Configuration(mt.etat_initial, rubans, [0] * mt.nb_rubans)


if __name__ == "__main__":
    mt = charger_mt("machines/q6_compare.tm")
    config = creer_configuration_initiale(mt, "10#11")
    print("Machine :", mt.nom)
    print("Rubans  :", config.rubans)
