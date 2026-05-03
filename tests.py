"""
Tests unitaires — Machine Universelle (Q1 à Q8)
Lancer : python -m pytest tests.py -v
      ou : python tests.py
"""
import unittest
import os
import sys

# S'assurer qu'on est dans le bon répertoire
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from exo1 import MT, Configuration
from exo2 import charger_mt, creer_configuration_initiale
from exo3 import un_pas_de_calcul
from exo4 import simuler_machine, extraire_resultat
from exo7 import coder_machine, parser_transitions, lire_lignes_utiles, _construire_table_renommage
from exo8 import texte_vers_binaire, binaire_vers_entier, afficher_codages


# ─────────────────────────────────────────────
# Q1 — Structures MT et Configuration
# ─────────────────────────────────────────────
class TestQ1Structures(unittest.TestCase):

    def test_creation_mt(self):
        mt = MT("test", {"q0", "qF"}, {"0", "1"}, {"0", "1", "_"},
                {}, "q0", {"qF"}, nb_rubans=1)
        self.assertEqual(mt.nom, "test")
        self.assertEqual(mt.etat_initial, "q0")
        self.assertEqual(mt.nb_rubans, 1)

    def test_est_final_vrai(self):
        mt = MT("t", set(), set(), set(), {}, "q0", {"qF"})
        self.assertTrue(mt.est_final("qF"))

    def test_est_final_faux(self):
        mt = MT("t", set(), set(), set(), {}, "q0", {"qF"})
        self.assertFalse(mt.est_final("q0"))

    def test_configuration_copier(self):
        config = Configuration("q0", [["a", "b", "_"]], [0])
        copie = config.copier()
        copie.rubans[0][0] = "X"  # modifier la copie
        # l'original ne doit pas être affecté
        self.assertEqual(config.rubans[0][0], "a")

    def test_configuration_multi_rubans(self):
        config = Configuration("q0", [["a"], ["b"]], [0, 0])
        self.assertEqual(len(config.rubans), 2)
        self.assertEqual(len(config.tetes), 2)


# ─────────────────────────────────────────────
# Q2 — Chargement d'une machine
# ─────────────────────────────────────────────
class TestQ2Chargement(unittest.TestCase):

    def test_charger_compare(self):
        mt = charger_mt("machines/q6_compare.tm")
        self.assertEqual(mt.nom, "Compare x<y")
        self.assertEqual(mt.etat_initial, "q0")
        self.assertIn("q8", mt.etats_finaux)
        self.assertEqual(mt.nb_rubans, 2)

    def test_charger_search(self):
        mt = charger_mt("machines/q6_search.tm")
        self.assertEqual(mt.nb_rubans, 2)

    def test_charger_mul(self):
        mt = charger_mt("machines/q6_unary_mul.tm")
        self.assertEqual(mt.nb_rubans, 3)

    def test_config_initiale_ruban0(self):
        mt = charger_mt("machines/q6_compare.tm")
        config = creer_configuration_initiale(mt, "10#11")
        self.assertEqual(config.etat, "q0")
        self.assertEqual(config.rubans[0], list("10#11") + ["_"])

    def test_config_initiale_rubans_vides(self):
        mt = charger_mt("machines/q6_compare.tm")
        config = creer_configuration_initiale(mt, "10#11")
        # Le ruban 2 doit être initialisé vide
        self.assertEqual(config.rubans[1], ["_"])

    def test_config_initiale_mot_vide(self):
        mt = charger_mt("machines/q6_compare.tm")
        config = creer_configuration_initiale(mt, "")
        self.assertEqual(config.rubans[0], ["_"])


# ─────────────────────────────────────────────
# Q3 — Un pas de calcul
# ─────────────────────────────────────────────
class TestQ3UnPas(unittest.TestCase):

    def setUp(self):
        self.mt = charger_mt("machines/q6_compare.tm")

    def test_un_pas_change_etat(self):
        config = creer_configuration_initiale(self.mt, "10#11")
        nouvelle = un_pas_de_calcul(self.mt, config)
        self.assertIsNotNone(nouvelle)
        # La tête avance ou l'état change
        self.assertTrue(
            nouvelle.etat != config.etat or nouvelle.tetes != config.tetes
        )

    def test_un_pas_etat_final_retourne_none(self):
        # Créer une config déjà en état final
        mt = charger_mt("machines/q6_compare.tm")
        config = Configuration("q8", [["_"], ["_"]], [0, 0])
        # est_final → True mais un_pas_de_calcul ne vérifie pas ça, il cherche une transition
        # Il doit retourner None car pas de transition depuis qAccept
        resultat = un_pas_de_calcul(mt, config)
        self.assertIsNone(resultat)

    def test_un_pas_sans_transition_retourne_none(self):
        mt = charger_mt("machines/q6_compare.tm")
        config = Configuration("qInexistant", [["0", "_"], ["_"]], [0, 0])
        self.assertIsNone(un_pas_de_calcul(mt, config))


# ─────────────────────────────────────────────
# Q4 — Simulation complète
# ─────────────────────────────────────────────
class TestQ4Simulation(unittest.TestCase):

    def test_compare_x_lt_y_accepte(self):
        """10 < 11 en binaire → la machine doit s'arrêter en état final"""
        mt = charger_mt("machines/q6_compare.tm")
        config = simuler_machine(mt, "10#11", max_etapes=500)
        self.assertTrue(mt.est_final(config.etat))

    def test_compare_x_ge_y_boucle(self):
        """11 >= 10 → la machine doit boucler (limite atteinte)"""
        mt = charger_mt("machines/q6_compare.tm")
        config = simuler_machine(mt, "11#10", max_etapes=300)
        self.assertFalse(mt.est_final(config.etat))

    def test_compare_egaux_boucle(self):
        """10 = 10 → boucle"""
        mt = charger_mt("machines/q6_compare.tm")
        config = simuler_machine(mt, "10#10", max_etapes=300)
        self.assertFalse(mt.est_final(config.etat))

    def test_search_trouve(self):
        """'10' dans [01, 10, 111] → arrêt"""
        mt = charger_mt("machines/q6_search.tm")
        config = simuler_machine(mt, "10#01#10#111", max_etapes=2000)
        self.assertTrue(mt.est_final(config.etat))

    def test_search_pas_trouve(self):
        """'11' absent de [01, 10, 00] → boucle"""
        mt = charger_mt("machines/q6_search.tm")
        config = simuler_machine(mt, "11#01#10#00", max_etapes=500)
        self.assertFalse(mt.est_final(config.etat))

    def test_mul_unaire_2x3(self):
        """1^2 * 1^3 = 1^6 → ruban de sortie contient 6 '1'"""
        mt = charger_mt("machines/q6_unary_mul.tm")
        config = simuler_machine(mt, "11#111", max_etapes=5000)
        self.assertTrue(mt.est_final(config.etat))
        resultat = extraire_resultat(config)
        nb_uns = resultat.count("1")
        self.assertEqual(nb_uns, 6)

    def test_mul_unaire_1x1(self):
        """1^1 * 1^1 = 1^1"""
        mt = charger_mt("machines/q6_unary_mul.tm")
        config = simuler_machine(mt, "1#1", max_etapes=500)
        self.assertTrue(mt.est_final(config.etat))
        self.assertEqual(extraire_resultat(config).count("1"), 1)

    def test_mul_unaire_3x4(self):
        """1^3 * 1^4 = 1^12"""
        mt = charger_mt("machines/q6_unary_mul.tm")
        config = simuler_machine(mt, "111#1111", max_etapes=10000)
        self.assertTrue(mt.est_final(config.etat))
        self.assertEqual(extraire_resultat(config).count("1"), 12)


# ─────────────────────────────────────────────
# Q7 — Codage <M>
# ─────────────────────────────────────────────
class TestQ7Codage(unittest.TestCase):

    def test_machine_multiruban_leve_erreur(self):
        with self.assertRaises(ValueError):
            coder_machine("machines/q6_compare.tm")

    def test_machine_3rubans_leve_erreur(self):
        with self.assertRaises(ValueError):
            coder_machine("machines/q6_unary_mul.tm")

    def test_swap_format_commence_par_0_1(self):
        """Le codage doit commencer par 0|1 (init=0, final=1)"""
        codage = coder_machine("machines/swap01.tm")
        parties = codage.split("|")
        self.assertEqual(parties[0], "0")   # état initial
        self.assertEqual(parties[1], "1")   # état final

    def test_swap_nb_champs_par_transition(self):
        """Chaque transition = 5 champs pour 1 ruban"""
        codage = coder_machine("machines/swap01.tm")
        parties = codage.split("|")
        # 2 premiers = init, final. Reste = transitions de 5 champs
        self.assertEqual((len(parties) - 2) % 5, 0)

    def test_swap_contient_blanc_unicode(self):
        """Le blanc '_' doit être remplacé par □ dans le codage"""
        codage = coder_machine("machines/swap01.tm")
        self.assertNotIn("_", codage)
        self.assertIn("\u25a1", codage)

    def test_renommage_init_est_0(self):
        """L'état initial doit être renommé 0"""
        lignes = lire_lignes_utiles("machines/swap01.tm")
        init, final, _, transitions = parser_transitions(lignes)
        table = _construire_table_renommage(init, final, transitions)
        self.assertEqual(table[init], "0")

    def test_renommage_final_est_1(self):
        """L'état final doit être renommé 1"""
        lignes = lire_lignes_utiles("machines/swap01.tm")
        init, final, _, transitions = parser_transitions(lignes)
        table = _construire_table_renommage(init, final, transitions)
        self.assertEqual(table[final], "1")


# ─────────────────────────────────────────────
# Q8 — Codage binaire
# ─────────────────────────────────────────────
class TestQ8CodageBinaire(unittest.TestCase):

    def test_texte_vers_binaire_ascii(self):
        """'A' en ASCII = 65 = 01000001"""
        self.assertEqual(texte_vers_binaire("A"), "01000001")

    def test_texte_vers_binaire_longueur(self):
        """n caractères ASCII → 8n bits"""
        texte = "abc"
        self.assertEqual(len(texte_vers_binaire(texte)), 24)

    def test_binaire_vers_entier_zero(self):
        self.assertEqual(binaire_vers_entier(""), 0)

    def test_binaire_vers_entier_simple(self):
        self.assertEqual(binaire_vers_entier("1010"), 10)

    def test_binaire_vers_entier_un(self):
        self.assertEqual(binaire_vers_entier("00000001"), 1)

    def test_codage_swap_entier_positif(self):
        """L'entier résultant du codage binaire de swap01 doit être > 0"""
        codage = coder_machine("machines/swap01.tm")
        entier = binaire_vers_entier(texte_vers_binaire(codage))
        self.assertGreater(entier, 0)

    def test_codage_binaire_decodable(self):
        """Le codage binaire doit être réversible via UTF-8"""
        texte_original = coder_machine("machines/swap01.tm")
        binaire = texte_vers_binaire(texte_original)
        # Reconvertir binaire → octets → texte
        octets = bytes(int(binaire[i:i+8], 2) for i in range(0, len(binaire), 8))
        texte_decode = octets.decode("utf-8")
        self.assertEqual(texte_original, texte_decode)


if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite  = unittest.TestSuite()

    for cls in [
        TestQ1Structures, TestQ2Chargement, TestQ3UnPas,
        TestQ4Simulation, TestQ7Codage, TestQ8CodageBinaire
    ]:
        suite.addTests(loader.loadTestsFromTestCase(cls))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)
