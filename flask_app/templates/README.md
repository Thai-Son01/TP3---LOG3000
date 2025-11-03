## templates/

Ce répertoire contient les **fichiers HTML** utilisés par l’application web.  

Actuellement, il contient seulement :

- `index.html` : la page principale de la calculatrice Flask, qui est affichée lorsque l'utilisateur accède à l'application.

> Flask utilise ce dossier pour rechercher automatiquement les templates lors de l'appel de `render_template()`.

### Ajouter une nouvelle page

Pour ajouter une nouvelle page à l'application :

1. Créez un nouveau fichier HTML dans le dossier `templates/`, par exemple `about.html` :


2. Définissez une route correspondante dans votre application Flask :

```python
@app.route('/about')
def about():
    return render_template('about.html')
