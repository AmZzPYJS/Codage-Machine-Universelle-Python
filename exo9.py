# Question 9 — Machine de Turing Universelle à 3 rubans
#
# Entrée : <M>#x sur le ruban 1
#   - <M> est le codage d'une machine mono-ruban au format de Q7 :
#     0|1|q|sym_lu|sym_écrit|dir|q'|...
#   - x est le mot d'entrée
#
# Les 3 rubans ont les rôles suivants :
#   Ruban 1 : contient <M>#x — lecture seule (on ne le modifie jamais)
#   Ruban 2 : simule le ruban de M (initialisé avec x)
#   Ruban 3 : contient l'état courant de M (encodé comme chaîne)
#
# Algorithme à chaque étape :
#   1. Lire l'état courant sur ruban 3
#   2. Lire le symbole sous la tête sur ruban 2
#   3. Parcourir <M> sur ruban 1 pour trouver la transition (état, symbole)
#   4. Appliquer : écrire le nouveau symbole sur ruban 2,
#      déplacer la tête, mettre à jour l'état sur ruban 3
#   5. Répéter jusqu'à atteindre l'état final "1"

BLANC = "_"
BLANC_CODAGE = "\u25a1"  # □ utilisé dans <M>


def decoder_machine(codage_M):
    """
    Parse le codage <M> produit par Q7.
    Format : 0|1|q|sym_lu|sym_écrit|dir|q'|...
    Retourne (etat_initial, etat_final, transitions).
    transitions = dict { (q, sym_lu) : (sym_écrit, dir, q') }
    """
    parties = codage_M.split("|")
    if len(parties) < 2:
        raise ValueError(f"Codage <M> invalide : {codage_M}")

    etat_initial = parties[0]
    etat_final   = parties[1]
    transitions  = {}

    i = 2
    while i + 4 < len(parties):
        q        = parties[i]
        sym_lu   = parties[i+1]
        sym_ecrit = parties[i+2]
        direction = parties[i+3]
        q2       = parties[i+4]
        # Reconvertir □ → _ pour la simulation
        sym_lu_sim   = BLANC if sym_lu   == BLANC_CODAGE else sym_lu
        sym_ecrit_sim = BLANC if sym_ecrit == BLANC_CODAGE else sym_ecrit
        transitions[(q, sym_lu_sim)] = (sym_ecrit_sim, direction, q2)
        i += 5

    return etat_initial, etat_final, transitions


def lire_symbole(ruban, tete):
    """Lit le symbole sous la tête (blanc si hors limites)."""
    if tete < 0 or tete >= len(ruban):
        return BLANC
    return ruban[tete]


def ecrire_symbole(ruban, tete, symbole):
    """Écrit un symbole sur le ruban, étend si nécessaire."""
    while tete >= len(ruban):
        ruban.append(BLANC)
    if tete < 0:
        ruban.insert(0, symbole)
    else:
        ruban[tete] = symbole


def deplacer_tete(tete, direction, ruban):
    """Déplace la tête selon la direction."""
    if direction == ">":
        tete += 1
    elif direction == "<":
        tete -= 1
        if tete < 0:
            ruban.insert(0, BLANC)
            tete = 0
    # "-" = rester sur place
    while tete >= len(ruban):
        ruban.append(BLANC)
    return tete


def machine_universelle(codage_entree, max_etapes=10000, verbose=False):
    """
    Machine de Turing Universelle à 3 rubans.
    
    Paramètres :
        codage_entree : str — entrée de la forme "<M>#x"
                        où <M> est le codage Q7 et x le mot d'entrée
        max_etapes    : int — limite de sécurité contre les boucles
        verbose       : bool — affiche chaque étape si True
    
    Retourne :
        (accepte: bool, ruban_final: list, nb_etapes: int)
    """
    # Séparer <M> et x
    separateur = codage_entree.find("#")
    if separateur == -1:
        raise ValueError("Format attendu : <M>#x")

    codage_M = codage_entree[:separateur]
    mot_x    = codage_entree[separateur+1:]

    # Décoder la machine M
    etat_initial, etat_final, transitions = decoder_machine(codage_M)

    # Initialiser les 3 rubans
    ruban2 = list(mot_x) if mot_x else [BLANC]  # ruban de simulation
    tete2  = 0
    etat_courant = etat_initial

    if verbose:
        print(f"Machine Universelle démarrée")
        print(f"  État initial : {etat_initial}, État final : {etat_final}")
        print(f"  Transitions disponibles : {len(transitions)}")
        print(f"  Mot d'entrée : '{mot_x}'")
        print()

    nb_etapes = 0

    while nb_etapes < max_etapes:
        # Vérifier si on est dans l'état final
        if etat_courant == etat_final:
            if verbose:
                print(f"→ État final '{etat_final}' atteint après {nb_etapes} étape(s).")
                print(f"→ Contenu du ruban : {''.join(ruban2).rstrip(BLANC)}")
            return True, ruban2, nb_etapes

        # Lire le symbole courant
        sym = lire_symbole(ruban2, tete2)

        # Chercher la transition
        cle = (etat_courant, sym)
        if cle not in transitions:
            # Pas de transition → machine bloquée
            if verbose:
                print(f"→ Bloquée à l'étape {nb_etapes} : pas de transition depuis ({etat_courant}, '{sym}').")
            return False, ruban2, nb_etapes

        sym_ecrit, direction, nouvel_etat = transitions[cle]

        if verbose:
            ruban_affiche = "".join(ruban2)
            curseur = " " * tete2 + "^"
            print(f"Étape {nb_etapes:4d} | État: {etat_courant:6s} | Lu: '{sym}' "
                  f"→ Écrit: '{sym_ecrit}', Dir: {direction}, Nouvel état: {nouvel_etat}")
            print(f"         Ruban: {ruban_affiche}")
            print(f"                {curseur}")

        # Appliquer la transition
        ecrire_symbole(ruban2, tete2, sym_ecrit)
        tete2 = deplacer_tete(tete2, direction, ruban2)
        etat_courant = nouvel_etat
        nb_etapes += 1

    # Limite atteinte → boucle infinie probable
    if verbose:
        print(f"→ Limite de {max_etapes} étapes atteinte — M boucle probablement sur '{mot_x}'.")
    return False, ruban2, nb_etapes


if __name__ == "__main__":
    from exo7 import coder_machine
    import os

    print("=" * 60)
    print("Test Q9 — Machine Universelle")
    print("=" * 60)

    if not os.path.exists("machines/swap01.tm"):
        print("Fichier machines/swap01.tm introuvable.")
    else:
        # Coder la machine swap01
        codage_M = coder_machine("machines/swap01.tm")
        print(f"Codage <M> de swap01 : {codage_M}")
        print()

        # Test 1 : simuler swap01 sur "010"
        entree = codage_M + "#010"
        print(f"Simulation de swap01 sur '010' (attendu : '101') :")
        accepte, ruban, nb_etapes = machine_universelle(entree, verbose=True)
        resultat = "".join(ruban).rstrip(BLANC)
        print(f"\nRésultat : '{resultat}' — {'✓' if resultat == '101' else '✗'}")
        print()

        # Test 2 : simuler swap01 sur "11"
        entree2 = codage_M + "#11"
        print(f"Simulation de swap01 sur '11' (attendu : '00') :")
        accepte2, ruban2, etapes2 = machine_universelle(entree2, verbose=False)
        resultat2 = "".join(ruban2).rstrip(BLANC)
        print(f"Résultat : '{resultat2}' — {'✓' if resultat2 == '00' else '✗'} ({etapes2} étapes)")
        print()

        # Test 3 : simuler swap01 sur mot vide
        entree3 = codage_M + "#"
        print(f"Simulation de swap01 sur '' (mot vide) :")
        accepte3, ruban3, etapes3 = machine_universelle(entree3, verbose=False)
        resultat3 = "".join(ruban3).rstrip(BLANC)
        print(f"Résultat : '{resultat3}' ({etapes3} étapes)")
