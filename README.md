<a id="readme-top"></a>
# Calculatrice Web Flask  
**Projet de l'équipe 51**

---

## Description

Cette application web est une calculatrice simple développée avec Flask.  
Elle permet d'effectuer des opérations arithmétiques de base (addition, soustraction, multiplication, division) via une interface utilisateur intuitive.  
Le projet vise à démontrer la création d’une application web dynamique en Python.

---

## Prérequis d'installation

Python 3.9 ou plus selon https://flask.palletsprojects.com/en/stable/installation/#python-version

## Guide d’installation

Suivez ces étapes pour installer et lancer l'application localement :

1. **Cloner le dépôt :**

```sh
git clone git@github.com:Thai-Son01/TP3---LOG3000.git
cd TP3---LOG3000
```
2. **(Optionnel) Créer et activer un environnement virtuel :**
```sh
python -m venv venv
venv/Scripts/activate
```
3. **Installer Flask :**
```sh
pip install Flask
```
## Guide d’utilisation
1. **Aller dans le répertoire de l'application**
```sh
cd flask_app
```
2. **Rouler le serveur dans un terminal et ouvrir le lien**
```sh
python -m flask --app ./flask_app/app run
```

- **Calcul d'un résultat :**  
  Cliquez, dans l'ordre, sur un nombre, un opérateur, un deuxième nombre, puis sur le bouton **"="** à la fin.

- **Réinitialisation :**  
  Le bouton **"C"** permet de réinitialiser la calculatrice.

- **Message d'erreur :**  
  Un message d'erreur apparaît en cas de saisie incorrecte ou d'opération invalide.


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

## Contribution

1. Créer une issue.
2. Assigner l'issue à vous-même.
3. Créer une branche à partir de l'issue et la nommer selon la nomenclature type/description (ex : fix/multiplication-incorrecte).
4. Mettre à jour la branche régulièrement avec le main.
5. Effectuer une pull request lorsque terminé.
6. Squash merge et supprimer la branche lorsque le merge est effectué.
