# Question 10 — Machine Universelle avec compteur d'étapes
#
# Extension de Q9 : la MU prend en entrée <M>#x#n et simule M sur x
# pendant AU PLUS n étapes.
#
# Le 4ème ruban sert de compteur : initialisé à n (en unaire : 1^n),
# on efface un '1' à chaque étape de simulation.
# Quand le compteur est vide (que des blancs), on s'arrête.
#
# Entrée : "<M>#x#n" où n est un entier en base 10

from exo9 import machine_universelle, decoder_machine, BLANC


def machine_universelle_bornee(codage_entree, max_etapes_securite=100000, verbose=False):
    """
    Machine de Turing Universelle bornée à 4 rubans.
    
    Entrée : "<M>#x#n"
        - <M> : codage Q7 de la machine
        - x   : mot d'entrée
        - n   : nombre maximal d'étapes (entier en base 10)
    
    Simule M sur x pendant au plus n étapes.
    
    Retourne :
        (accepte: bool, ruban_final: list, nb_etapes_effectuees: int, raison_arret: str)
        raison_arret : "final" | "compteur_epuise" | "bloquee" | "securite"
    """
    # Parser l'entrée <M>#x#n
    parties = codage_entree.split("#", 2)
    if len(parties) != 3:
        raise ValueError("Format attendu : <M>#x#n")

    codage_M, mot_x, n_str = parties

    try:
        n = int(n_str)
    except ValueError:
        raise ValueError(f"n doit être un entier, reçu : '{n_str}'")

    if n < 0:
        raise ValueError(f"n doit être positif, reçu : {n}")

    # Décoder M
    etat_initial, etat_final, transitions = decoder_machine(codage_M)

    # Initialiser le ruban de simulation (ruban 2)
    ruban = list(mot_x) if mot_x else [BLANC]
    tete  = 0
    etat_courant = etat_initial

    # Compteur d'étapes (ruban 4) : on utilise simplement un entier Python
    # (équivalent à un ruban unaire 1^n qu'on décrémente à chaque étape)
    compteur = n
    nb_etapes = 0

    if verbose:
        print(f"MU bornée : simulation de M sur '{mot_x}' pendant au plus {n} étape(s)")
        print(f"  État initial : {etat_initial}, État final : {etat_final}")
        print()

    while nb_etapes < max_etapes_securite:

        # Vérifier état final
        if etat_courant == etat_final:
            if verbose:
                print(f"→ État final atteint après {nb_etapes} étape(s).")
            return True, ruban, nb_etapes, "final"

        # Vérifier compteur
        if compteur <= 0:
            if verbose:
                print(f"→ Compteur épuisé après {nb_etapes} étape(s) — M ne s'est pas arrêtée en {n} étapes.")
            return False, ruban, nb_etapes, "compteur_epuise"

        # Lire symbole
        sym = ruban[tete] if 0 <= tete < len(ruban) else BLANC

        # Chercher transition
        cle = (etat_courant, sym)
        if cle not in transitions:
            if verbose:
                print(f"→ Bloquée à l'étape {nb_etapes}.")
            return False, ruban, nb_etapes, "bloquee"

        sym_ecrit, direction, nouvel_etat = transitions[cle]

        if verbose:
            print(f"Étape {nb_etapes:4d} | Compteur: {compteur:4d} | "
                  f"({etat_courant}, '{sym}') → ('{sym_ecrit}', {direction}, {nouvel_etat})")

        # Appliquer transition
        while tete >= len(ruban): ruban.append(BLANC)
        ruban[tete] = sym_ecrit

        if direction == ">":
            tete += 1
        elif direction == "<":
            tete -= 1
            if tete < 0:
                ruban.insert(0, BLANC)
                tete = 0
        while tete >= len(ruban): ruban.append(BLANC)

        etat_courant = nouvel_etat
        compteur -= 1   # décrémenter le compteur (ruban 4)
        nb_etapes += 1

    return False, ruban, nb_etapes, "securite"


if __name__ == "__main__":
    from exo7 import coder_machine
    import os

    print("=" * 60)
    print("Test Q10 — Machine Universelle Bornée")
    print("=" * 60)

    if not os.path.exists("machines/swap01.tm"):
        print("Fichier machines/swap01.tm introuvable.")
    else:
        codage_M = coder_machine("machines/swap01.tm")

        # Test 1 : n suffisant → doit s'arrêter
        print("Test 1 : swap01 sur '010', n=10 (suffisant)")
        entree = f"{codage_M}#010#10"
        accepte, ruban, etapes, raison = machine_universelle_bornee(entree, verbose=True)
        print(f"Résultat : '{''.join(ruban).rstrip(BLANC)}' | Raison: {raison} | Étapes: {etapes}\n")

        # Test 2 : n trop petit → compteur épuisé
        print("Test 2 : swap01 sur '010', n=1 (trop petit)")
        entree2 = f"{codage_M}#010#1"
        accepte2, ruban2, etapes2, raison2 = machine_universelle_bornee(entree2, verbose=True)
        print(f"Résultat : '{''.join(ruban2).rstrip(BLANC)}' | Raison: {raison2} | Étapes: {etapes2}\n")

        # Test 3 : n=0 → arrêt immédiat
        print("Test 3 : swap01 sur '010', n=0")
        entree3 = f"{codage_M}#010#0"
        accepte3, ruban3, etapes3, raison3 = machine_universelle_bornee(entree3, verbose=False)
        print(f"Résultat : Raison={raison3} | Étapes={etapes3}\n")

        # Test 4 : mot vide, n=5
        print("Test 4 : swap01 sur '', n=5")
        entree4 = f"{codage_M}##5"
        accepte4, ruban4, etapes4, raison4 = machine_universelle_bornee(entree4, verbose=False)
        print(f"Résultat : '{''.join(ruban4).rstrip(BLANC)}' | Raison: {raison4} | Étapes: {etapes4}")
