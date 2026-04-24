# Question 7 — Codage <M> d'une machine de Turing (format de l'énoncé, section 2)
#
# Format de sortie :
#   0 | 1 | q_courant | sym_lu | sym_écrit | direction | q_suivant | ...
#
# Conformément au cours (Strozecki, section 2) :
#   - L'état initial est TOUJOURS codé par "0"
#   - L'état final   est TOUJOURS codé par "1"
#   - Les autres états reçoivent un entier ≥ 2 par ordre de découverte
#   - Le blanc '_' est représenté par '□'
#   - Les directions >, <, - sont conservées telles quelles
#
# Exemple du cours : machine qui swape 0↔1
#   0|□|□|-|1|0|0|1|>|0|0|1|0|>|0
#
# Réponse à la question ouverte (alphabet quelconque) :
#   On numérote chaque symbole de Γ et on le remplace par son index en binaire
#   sur k = ⌈log2|Γ|⌉ bits (cf. théorème du cours sur l'équivalence des alphabets).
#   Le séparateur '|' ne peut pas apparaître dans un symbole binaire → pas d'ambiguïté.

BLANC_AFFICHE = "\u25a1"  # □


def nettoyer_ligne(ligne):
    if "//" in ligne:
        ligne = ligne.split("//")[0]
    return ligne.strip()


def lire_lignes_utiles(nom_fichier):
    with open(nom_fichier, "r", encoding="utf-8") as f:
        return [l for ligne in f if (l := nettoyer_ligne(ligne))]


def symbole_vers_codage(s):
    return BLANC_AFFICHE if s == "_" else s


def parser_transitions(lignes_utiles):
    """
    Parse le fichier .tm et retourne :
      (etat_initial, etat_final, nb_rubans, transitions)
    Chaque transition : (etat_courant, sym_lus, sym_ecrits, directions, etat_suivant)
    """
    etat_initial = etat_final = None
    transitions = []
    nb_rubans = None
    i = 0

    while i < len(lignes_utiles):
        ligne = lignes_utiles[i]
        if ligne.startswith("name:"):  i += 1; continue
        if ligne.startswith("init:"):
            etat_initial = ligne.split(":", 1)[1].strip(); i += 1; continue
        if ligne.startswith("accept:"):
            etat_final = ligne.split(":", 1)[1].strip().split(",")[0].strip()
            i += 1; continue

        if "," in ligne and i + 1 < len(lignes_utiles):
            lecture  = [x.strip() for x in ligne.split(",") if x.strip()]
            ecriture = [x.strip() for x in lignes_utiles[i+1].split(",") if x.strip()]
            etat_courant = lecture[0]
            sym_lus = lecture[1:]
            k = len(sym_lus)

            if nb_rubans is None:
                nb_rubans = k
            elif nb_rubans != k:
                raise ValueError(f"Incohérence rubans : attendu {nb_rubans}, trouvé {k}")

            if len(ecriture) != 1 + 2 * k:
                i += 1; continue

            transitions.append((
                etat_courant, sym_lus,
                ecriture[1:1+k], ecriture[1+k:1+2*k], ecriture[0]
            ))
            i += 2; continue
        i += 1

    return etat_initial, etat_final, nb_rubans or 1, transitions


def _construire_table_renommage(etat_initial, etat_final, transitions):
    """
    Renomme les états pour que :
      - l'état initial  → "0"
      - l'état final    → "1"
      - les autres      → "2", "3", ... par ordre d'apparition
    Conforme à la convention du cours (section 2 de l'énoncé).
    """
    table = {etat_initial: "0", etat_final: "1"}
    compteur = 2

    tous_etats = []
    for (q, _, _, _, q2) in transitions:
        tous_etats.append(q)
        tous_etats.append(q2)

    for etat in tous_etats:
        if etat not in table:
            table[etat] = str(compteur)
            compteur += 1

    return table


def coder_machine(nom_fichier):
    """
    Produit le codage <M> d'une machine MONO-RUBAN (section 2 de l'énoncé).
    Format : 0|1|q|sym_lu|sym_écrit|dir|q'|...
    Les états sont renommés : initial→0, final→1, autres→2,3,...
    Lève ValueError si la machine a plus d'un ruban.
    """
    lignes = lire_lignes_utiles(nom_fichier)
    etat_initial, etat_final, nb_rubans, transitions = parser_transitions(lignes)

    if nb_rubans != 1:
        raise ValueError(
            f"Codage <M> réservé aux machines mono-ruban (section 2). "
            f"Cette machine a {nb_rubans} rubans."
        )
    if not etat_initial or not etat_final:
        raise ValueError("État initial ou final manquant.")

    table = _construire_table_renommage(etat_initial, etat_final, transitions)

    parties = ["0", "1"]  # init=0, final=1 — convention du cours
    for (q, sym_lus, sym_ecrits, directions, q2) in transitions:
        parties += [
            table[q],
            symbole_vers_codage(sym_lus[0]),
            symbole_vers_codage(sym_ecrits[0]),
            directions[0],
            table[q2]
        ]

    return "|".join(parties)


if __name__ == "__main__":
    import os

    # Test sur la machine mono-ruban swap01 (exemple du cours)
    if os.path.exists("machines/swap01.tm"):
        print("=== swap01.tm (mono-ruban — exemple du cours) ===")
        print(coder_machine("machines/swap01.tm"))
        print()

    # Les 3 machines Q6 sont multi-rubans → ValueError attendue
    for fichier, label in [
        ("machines/q6_compare.tm",   "q6_compare   (2 rubans)"),
        ("machines/q6_search.tm",    "q6_search    (2 rubans)"),
        ("machines/q6_unary_mul.tm", "q6_unary_mul (3 rubans)"),
    ]:
        print(f"=== {label} ===")
        try:
            print(coder_machine(fichier))
        except ValueError as e:
            print(f"[OK] Erreur attendue : {e}")
        print()
