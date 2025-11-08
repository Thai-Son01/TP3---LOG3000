# Tests

Ce dossier contient tous les tests unitaires de l'application Flask. Tous les tests sont réalisés avec le framework intégré unittest de Python.

## Structure

- `test_app.py` – Tests pour l'application principale et ses routes.
- `test_operators.py` – Tests pour la logique de calcul.

## Guide de tests
Toutes les commandes sont executées à partir du répertoire TP3---LOG3000
- Pour rouler tous les tests :
```
python -m unittest discover
```
- Pour rouler un fichier de test en particulier :
```
python -m unittest discover -s flask_app/tests -t . -p NOM_FICHIER_PYTHON.py
```
