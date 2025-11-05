from flask import Flask, request, render_template
from flask_app.operators import add, subtract, multiply, divide

app = Flask(__name__)

OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
        Une fonction qui évalue une expression arithmétique simple contenant deux opérandes numériques 
        et un seul opérateur (+, -, *, /).

        Arguments :
            expr (str) : Une chaîne de caractères représentant l'expression arithmétique 
                        (par exemple : "2 + 3" ou "10/5").

        Retourne :
            Le résultat de l'opération.

        Lève :
            ValueError : Si l'expression est vide, contient plus d’un opérateur,
                        présente un format invalide ou inclut des opérandes non numériques.
    """

    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None
    
    # On vérifie qu'il n'y a qu'un seul opérateur mathématique, 
    # car on ne gère que des expressions simples (un opérateur et deux opérandes).
    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1: 
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    # On vérifie que l'opérateur n'est ni au début ni à la fin de l'expression, 
    # et qu'il existe bien entre deux opérandes.
    if op_pos <= 0 or op_pos >= len(s) - 1:
        raise ValueError("invalid expression format")

    # On récupère les opérandes de l'expression. 
    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Gère la page principale de l'application (route '/').
    
    Cette fonction affiche le formulaire de la calculatrice et traite les entrées de l'utilisateur.
    - En méthode GET : affiche simplement la page.
    - En méthode POST : récupère l'expression envoyée par le formulaire, tente de la calculer,
      puis renvoie le résultat ou un message d'erreur.

    Retourne :
        Le modèle HTML 'index.html' avec le résultat du calcul (ou un message d'erreur).
    """
    result = "" 

    if request.method == 'POST':
        expression = request.form.get('display', '')

        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)