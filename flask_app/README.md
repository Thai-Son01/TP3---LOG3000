# Application web de calculatrice avec Flask

Ce projet est une application web simple de calculatrice développée avec Flask.

---

## Structure des dossiers

- `static/`  
  Ce dossier contient les fichiers statiques de l'application, comme les feuilles de style CSS et les images.

- `templates/`  
  Ce dossier contient les fichiers HTML utilisés par Flask pour rendre les pages web. Ici se trouve notamment le fichier `index.html`, qui sert de page principale de l'application.

- `tests/`  
  Ce dossier contient les tests unitaires pour l'application.
---

## Fichiers Python

- `app.py`  
  C'est le fichier principal de l'application Flask. Il gère les routes web, récupère les entrées utilisateur via les formulaires, appelle les fonctions de calcul, et retourne les résultats affichés.

- `operators.py`  
  Ce fichier contient les fonctions de base pour les opérations arithmétiques (addition, soustraction, multiplication, division) utilisées par l'application.

---

Cette organisation permet de séparer clairement la logique backend (Python) des ressources frontend (HTML, CSS).
