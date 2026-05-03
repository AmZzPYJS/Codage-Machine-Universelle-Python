# Question 1 — Structures de données pour une Machine de Turing
# MT : description statique de la machine (états, transitions, alphabets)
# Configuration : état dynamique à un instant T (rubans, têtes, état courant)

class MT:
    def __init__(self, nom, etats, alphabet, alphabet_de_travail,
                 transitions, etat_initial, etats_finaux, nb_rubans=1):
        self.nom = nom
        self.etats = etats
        self.alphabet = alphabet
        self.alphabet_de_travail = alphabet_de_travail
        self.transitions = transitions
        self.etat_initial = etat_initial
        self.etats_finaux = etats_finaux
        self.nb_rubans = nb_rubans

    def est_final(self, etat):
        return etat in self.etats_finaux


class Configuration:
    def __init__(self, etat, rubans, tetes):
        self.etat = etat
        self.rubans = rubans
        self.tetes = tetes

    def copier(self):
        # Copie profonde : chaque ruban est copié indépendamment
        nouveaux_rubans = [ruban[:] for ruban in self.rubans]
        nouvelles_tetes = self.tetes[:]
        return Configuration(self.etat, nouveaux_rubans, nouvelles_tetes)
