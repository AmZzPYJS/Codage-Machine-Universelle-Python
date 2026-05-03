# Question 10 — Machine Universelle bornée à 4 rubans
# Prend en entrée <M>#x#n et simule M sur x pendant au plus n étapes
# Le 4ème ruban est un compteur décrémenté à chaque étape

from exo9 import decoder_machine, lire_symbole, ecrire_symbole, deplacer_tete, BLANC


def machine_universelle_bornee(codage_entree, max_etapes_securite=100000, verbose=False):
    # Simule M sur x pendant au plus n étapes à partir de "<M>#x#n"
    parties = codage_entree.split("#", 2)
    if len(parties) != 3:
        raise ValueError("Format attendu : <M>#x#n")

    codage_M, mot_x, n_str = parties
    try:
        n = int(n_str)
    except ValueError:
        raise ValueError(f"n doit être un entier, reçu : '{n_str}'")

    etat_initial, etat_final, transitions = decoder_machine(codage_M)

    ruban = list(mot_x) if mot_x else [BLANC]
    tete  = 0
    etat_courant = etat_initial
    compteur = n
    nb_etapes = 0

    if verbose:
        print(f"MU bornée : simulation de M sur '{mot_x}' pendant au plus {n} étape(s)")

    while nb_etapes < max_etapes_securite:
        if etat_courant == etat_final:
            if verbose:
                print(f"→ État final atteint après {nb_etapes} étape(s).")
            return True, ruban, nb_etapes, "final"

        if compteur <= 0:
            if verbose:
                print(f"→ Compteur épuisé après {nb_etapes} étape(s).")
            return False, ruban, nb_etapes, "compteur_epuise"

        sym = ruban[tete] if 0 <= tete < len(ruban) else BLANC
        cle = (etat_courant, sym)

        if cle not in transitions:
            if verbose:
                print(f"→ Bloquée à l'étape {nb_etapes}.")
            return False, ruban, nb_etapes, "bloquee"

        sym_ecrit, direction, nouvel_etat = transitions[cle]

        if verbose:
            print(f"Étape {nb_etapes:4d} | Compteur: {compteur:4d} | "
                  f"({etat_courant}, '{sym}') → ('{sym_ecrit}', {direction}, {nouvel_etat})")

        while tete >= len(ruban): ruban.append(BLANC)
        ruban[tete] = sym_ecrit
        tete = deplacer_tete(tete, direction, ruban)
        etat_courant = nouvel_etat
        compteur -= 1
        nb_etapes += 1

    return False, ruban, nb_etapes, "securite"


if __name__ == "__main__":
    from exo7 import coder_machine
    import os

    if os.path.exists("machines/swap01.tm"):
        codage_M = coder_machine("machines/swap01.tm")

        print("=== swap01 sur '010', n=10 (suffisant) ===")
        accepte, ruban, etapes, raison = machine_universelle_bornee(
            f"{codage_M}#010#10", verbose=True)
        print(f"Résultat : '{''.join(ruban).rstrip(BLANC)}' | Raison: {raison}\n")

        print("=== swap01 sur '010', n=1 (trop petit) ===")
        accepte2, ruban2, etapes2, raison2 = machine_universelle_bornee(
            f"{codage_M}#010#1", verbose=True)
        print(f"Résultat : Raison={raison2} | Étapes={etapes2}")
