# Question 9 — Machine de Turing Universelle à 3 rubans
# Prend en entrée <M>#x et simule M sur x
# Ruban 1 : <M>#x (lecture seule)
# Ruban 2 : simule le ruban de M
# Ruban 3 : contient l'état courant de M

BLANC = "_"
BLANC_CODAGE = "\u25a1"  # □


def decoder_machine(codage_M):
    # Parse le codage <M> de Q7 : "0|1|q|sym_lu|sym_écrit|dir|q'|..."
    parties = codage_M.split("|")
    if len(parties) < 2:
        raise ValueError(f"Codage <M> invalide : {codage_M}")
    etat_initial = parties[0]
    etat_final   = parties[1]
    transitions  = {}
    i = 2
    while i + 4 < len(parties):
        q, sym_lu, sym_ecrit, direction, q2 = (
            parties[i], parties[i+1], parties[i+2], parties[i+3], parties[i+4]
        )
        sym_lu_sim    = BLANC if sym_lu    == BLANC_CODAGE else sym_lu
        sym_ecrit_sim = BLANC if sym_ecrit == BLANC_CODAGE else sym_ecrit
        transitions[(q, sym_lu_sim)] = (sym_ecrit_sim, direction, q2)
        i += 5
    return etat_initial, etat_final, transitions


def lire_symbole(ruban, tete):
    # Retourne blanc si hors limites (ruban infini)
    if tete < 0 or tete >= len(ruban):
        return BLANC
    return ruban[tete]


def ecrire_symbole(ruban, tete, symbole):
    while tete >= len(ruban):
        ruban.append(BLANC)
    if tete < 0:
        ruban.insert(0, symbole)
    else:
        ruban[tete] = symbole


def deplacer_tete(tete, direction, ruban):
    # Déplace la tête et étend le ruban si nécessaire
    if direction == ">":
        tete += 1
    elif direction == "<":
        tete -= 1
        if tete < 0:
            ruban.insert(0, BLANC)
            tete = 0
    while tete >= len(ruban):
        ruban.append(BLANC)
    return tete


def machine_universelle(codage_entree, max_etapes=10000, verbose=False):
    # Simule M sur x à partir de l'entrée "<M>#x"
    separateur = codage_entree.find("#")
    if separateur == -1:
        raise ValueError("Format attendu : <M>#x")

    codage_M = codage_entree[:separateur]
    mot_x    = codage_entree[separateur+1:]

    etat_initial, etat_final, transitions = decoder_machine(codage_M)

    ruban2 = list(mot_x) if mot_x else [BLANC]
    tete2  = 0
    etat_courant = etat_initial

    if verbose:
        print(f"MU démarrée | init={etat_initial} | final={etat_final} | mot='{mot_x}'")

    nb_etapes = 0
    while nb_etapes < max_etapes:
        if etat_courant == etat_final:
            if verbose:
                print(f"→ État final atteint après {nb_etapes} étape(s).")
                print(f"→ Ruban : {''.join(ruban2).rstrip(BLANC)}")
            return True, ruban2, nb_etapes

        sym = lire_symbole(ruban2, tete2)
        cle = (etat_courant, sym)

        if cle not in transitions:
            if verbose:
                print(f"→ Bloquée à l'étape {nb_etapes} : pas de transition depuis ({etat_courant}, '{sym}').")
            return False, ruban2, nb_etapes

        sym_ecrit, direction, nouvel_etat = transitions[cle]

        if verbose:
            print(f"Étape {nb_etapes:4d} | ({etat_courant}, '{sym}') → ('{sym_ecrit}', {direction}, {nouvel_etat})")

        ecrire_symbole(ruban2, tete2, sym_ecrit)
        tete2 = deplacer_tete(tete2, direction, ruban2)
        etat_courant = nouvel_etat
        nb_etapes += 1

    if verbose:
        print(f"→ Limite de {max_etapes} étapes atteinte.")
    return False, ruban2, nb_etapes


if __name__ == "__main__":
    from exo7 import coder_machine
    import os

    if os.path.exists("machines/swap01.tm"):
        codage_M = coder_machine("machines/swap01.tm")
        print(f"Codage <M> : {codage_M}\n")

        print("=== swap01 sur '010' (attendu : '101') ===")
        _, ruban, etapes = machine_universelle(codage_M + "#010", verbose=True)
        print(f"Résultat : '{''.join(ruban).rstrip(BLANC)}'\n")

        print("=== swap01 sur '11' (attendu : '00') ===")
        _, ruban2, etapes2 = machine_universelle(codage_M + "#11")
        print(f"Résultat : '{''.join(ruban2).rstrip(BLANC)}' ({etapes2} étapes)")
