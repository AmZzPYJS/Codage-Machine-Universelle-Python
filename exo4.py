# Question 4 — Simuler la machine jusqu'à l'état final

from exo2 import creer_configuration_initiale
from exo3 import un_pas_de_calcul


def extraire_resultat(config):
    """
    Extrait le contenu utile du ruban 0 (ou du dernier ruban pour les machines
    qui écrivent leur résultat sur un ruban séparé) en supprimant les blancs de fin.
    Retourne une chaîne de caractères.
    """
    ruban = config.rubans[-1]  # dernier ruban = ruban de sortie
    contenu = "".join(ruban).rstrip("_")
    return contenu if contenu else "_"


def simuler_machine(mt, mot, max_etapes=10000):
    """
    Simule la machine mt sur le mot jusqu'à atteindre l'état final ou la limite d'étapes.
    Retourne la configuration finale.
    """
    config = creer_configuration_initiale(mt, mot)
    compteur = 0

    while True:
        if mt.est_final(config.etat):
            print(f"Machine arrêtée dans l'état final '{config.etat}' après {compteur} étape(s).")
            print(f"Résultat (ruban de sortie) : {extraire_resultat(config)}")
            return config

        if compteur >= max_etapes:
            print(f"Limite de {max_etapes} étapes atteinte — la machine boucle probablement.")
            return config

        nouvelle_config = un_pas_de_calcul(mt, config)

        if nouvelle_config is None:
            print(f"Machine bloquée à l'étape {compteur} (aucune transition depuis '{config.etat}').")
            return config

        config = nouvelle_config
        compteur += 1


if __name__ == "__main__":
    from exo2 import charger_mt

    mt = charger_mt("machines/q6_compare.tm")
    print("=== Comparaison 10 < 11 (attendu : arrêt) ===")
    simuler_machine(mt, "10#11", 1000)

    print("\n=== Comparaison 11 < 10 (attendu : boucle) ===")
    simuler_machine(mt, "11#10", 200)
