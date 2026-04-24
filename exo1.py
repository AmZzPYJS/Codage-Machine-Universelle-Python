class MT:
    def __init__(self, etats, alphabet, alphabet_de_travail, transitions, etat_initial, etat_final, nb_rubans=1):
        self.etats = etats 
        self.alphabet = alphabet
        self.alphabet_de_travail = alphabet_de_travail 
        self.transitions = transitions
        self.etat_initial = etat_initial
        self.etat_final = etat_final
        self.nb_rubans = nb_rubans

mt = MT(etats={'q0', 'q1'}, 
        alphabet={'0','1'}, 
        alphabet_de_travail={'0','1','#','|','_'}, 
        transitions = {('q0', '0'): ('q1', '1', 'R'),('q1', '1'): ('q0', '0', 'L')},
        etat_initial = 'q0',
        etat_final = 'q1')

class Configuration:
    def __init__(self, etat, ruban, tete):
        self.etat = etat
        self.ruban = ruban
        self.tete = tete

config = Configuration(
    etat='q0',
    ruban=['1', '0', '1', '_'],
    tete=1
)