# Projet — Machine Universelle (IN620)

Licence 3 Informatique — UVSQ / Université Paris-Saclay  
Module : IN620 — Calculabilité · 2025-2026

## Groupe

| Nom | Questions |
|---|---|
| MEZOUER Amîn | Q1, Q2, Q3, Q4 |
| Abdallah | Q5, Q6, Q7, Q8 |
| Moussa | Q9, Q10, Q11 |

## Prérequis

- Python 3.10+ (aucune dépendance externe)
- Docker + Docker Compose (optionnel)

---

## Lancer le projet

### Une commande par question

```bash
python main.py q2 machines/q6_compare.tm 10#11
python main.py q3 machines/q6_compare.tm 10#11
python main.py q4 machines/q6_compare.tm 10#11
python main.py q5 machines/q6_compare.tm 10#11
python main.py q6_compare
python main.py q6_search
python main.py q6_mul
python main.py q7 machines/swap01.tm
python main.py q8 machines/swap01.tm
```

### Tests unitaires (36 tests, Q1→Q8)

```bash
python tests.py
# ou :
python -m pytest tests.py -v
```

### Visualiseur HTML (bonus)

Ouvrir `visualizer.html` dans un navigateur — simulation animée des 3 machines Q6 avec contrôle pas-à-pas.

### Docker (bonus)

```bash
# Tests dans un conteneur
docker compose run tests

# Simulation interactive
docker compose run simulate q4 machines/q6_compare.tm 10#11

# Visualiseur sur http://localhost:8080
docker compose up visualizer
```

---

## Format des fichiers `.tm`

Format [turingmachinesimulator.com](https://turingmachinesimulator.com/). Commentaires : `//`. Blanc : `_`.

## Notes

- **Q7/Q8** : le codage `<M>` (section 2 de l'énoncé) est réservé aux machines **mono-ruban**. Les états sont renommés : initial → `0`, final → `1`, autres → `2`, `3`... (convention du cours Strozecki). Les machines Q6 étant multi-rubans, une `ValueError` est levée intentionnellement.
- `machine.txt` : brouillon au format maison, non utilisé dans le projet.
- `max_etapes=10000` par défaut pour détecter les boucles infinies.
