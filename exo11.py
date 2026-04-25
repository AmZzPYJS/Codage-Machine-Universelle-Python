# Question 11 — Décidabilité et indécidabilité de L1, L2, L3
#
# Cette question est THÉORIQUE. Le code ci-dessous illustre les preuves
# par des démonstrations pratiques, mais l'essentiel est dans les commentaires.
#
# ══════════════════════════════════════════════════════════════════════
# L1 = { <M>#n | M s'arrête sur n en moins de n étapes }
# ══════════════════════════════════════════════════════════════════════
# DÉCIDABLE
#
# Preuve :
#   On construit une machine D1 qui, sur l'entrée <M>#n :
#   1. Simule M sur n pendant AU PLUS n étapes (grâce à Q10)
#   2. Si M s'arrête avant n étapes → ACCEPTE
#   3. Sinon (compteur épuisé ou bloquée) → REJETTE
#
#   D1 termine toujours car la simulation est bornée par n étapes.
#   Donc L1 est décidable. □
#
# ══════════════════════════════════════════════════════════════════════
# L2 = { <M>#n | M s'arrête sur tous les mots de taille n }
# ══════════════════════════════════════════════════════════════════════
# INDÉCIDABLE
#
# Preuve par réduction depuis le problème de l'arrêt (ATM) :
#
#   Rappel : ATM = { <M>#w | M s'arrête sur w } est indécidable.
#
#   Supposons par l'absurde qu'il existe D2 qui décide L2.
#   On construit une machine R qui décide ATM :
#
#   Sur l'entrée <M>#w :
#     1. Construire une machine M' définie ainsi :
#        - Sur toute entrée y de taille |w| :
#            * Effacer y du ruban
#            * Simuler M sur w
#            * Si M s'arrête → s'arrêter
#        - Sur toute entrée y de taille ≠ |w| : boucler
#     2. Lancer D2 sur <M'>#|w|
#     3. Si D2 accepte → M' s'arrête sur tous les mots de taille |w|
#                      → M s'arrête sur w → ACCEPTER
#        Si D2 rejette → M ne s'arrête pas sur w → REJETER
#
#   R déciderait ATM, contradiction. Donc L2 est indécidable. □
#
# ══════════════════════════════════════════════════════════════════════
# L3 = { <M>#x#y | M calcule la même chose sur x et y }
# ══════════════════════════════════════════════════════════════════════
# INDÉCIDABLE
#
# Preuve par le théorème de Rice :
#
#   Le théorème de Rice énonce :
#   "Toute propriété non triviale de la fonction calculée par une MT
#    est indécidable."
#
#   La propriété P = "M calcule la même chose sur x et y" est :
#   - Une propriété de la FONCTION calculée par M (pas de M elle-même)
#   - Non triviale :
#       * Il existe des machines qui calculent la même chose sur x et y
#         (ex: machine qui ignore son entrée et retourne toujours ε)
#       * Il existe des machines qui calculent des choses différentes
#         (ex: machine identité : f(x) = x ≠ y = f(y) si x ≠ y)
#
#   Par le théorème de Rice, L3 est indécidable. □

from exo10 import machine_universelle_bornee
from exo7 import coder_machine
import os


def decider_L1(codage_M, n, verbose=False):
    """
    Décideur pour L1 = { <M>#n | M s'arrête sur n en moins de n étapes }.
    
    Stratégie : simuler M sur n pendant au plus n étapes.
    Si M s'arrête → True, sinon → False.
    Termine toujours (simulation bornée). → L1 est DÉCIDABLE.
    """
    n_int = int(n)
    entree = f"{codage_M}#{n}#{n_int + 1}"

    accepte, _, etapes, raison = machine_universelle_bornee(entree, verbose=verbose)

    if raison == "final":
        if verbose:
            print(f"L1 : M s'arrête sur '{n}' en {etapes} étape(s) < {n_int} → ACCEPTE")
        return True
    else:
        if verbose:
            print(f"L1 : M ne s'arrête pas sur '{n}' en {n_int} étapes (raison: {raison}) → REJETTE")
        return False


if __name__ == "__main__":
    print("=" * 60)
    print("Question 11 — Décidabilité / Indécidabilité")
    print("=" * 60)

    print("""
┌─────────────────────────────────────────────────────────┐
│  L1 = {<M>#n | M s'arrête sur n en moins de n étapes}  │
│  → DÉCIDABLE                                            │
│  Preuve : simulation bornée à n étapes, toujours finie  │
└─────────────────────────────────────────────────────────┘
""")

    print("""
┌─────────────────────────────────────────────────────────┐
│  L2 = {<M>#n | M s'arrête sur tous les mots de taille n}│
│  → INDÉCIDABLE                                          │
│  Preuve : réduction depuis ATM (problème de l'arrêt)    │
│  Si D2 décidait L2, on déciderait ATM → contradiction   │
└─────────────────────────────────────────────────────────┘
""")

    print("""
┌─────────────────────────────────────────────────────────┐
│  L3 = {<M>#x#y | M calcule la même chose sur x et y}   │
│  → INDÉCIDABLE                                          │
│  Preuve : théorème de Rice                              │
│  P est une propriété non triviale de la fonction de M   │
└─────────────────────────────────────────────────────────┘
""")

    # Démonstration pratique de L1
    if os.path.exists("machines/swap01.tm"):
        print("=" * 60)
        print("Démonstration pratique — L1")
        print("=" * 60)
        codage_M = coder_machine("machines/swap01.tm")

        # swap01 sur "0" : devrait s'arrêter rapidement
        print("\nTest : swap01 sur '0', n=10")
        print("→ M s'arrête sur '0' en moins de 10 étapes ?", decider_L1(codage_M, "0", verbose=True))

        # swap01 sur "01" avec n=1 : trop court
        print("\nTest : swap01 sur '01', n=1")
        print("→ M s'arrête sur '01' en moins de 1 étape ?", decider_L1(codage_M, "01", verbose=True))
