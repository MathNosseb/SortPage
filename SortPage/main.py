from flask import Flask, render_template, redirect, url_for, request, flash
import json
import urllib.parse
app = Flask(__name__)
app.secret_key="secret"#obligatoire pour l'utilisation de jinja
"""
Définition des décorateurs pour la redirection et leurs méthodes
"""

#decorateur racine
@app.route('/',
            methods=['GET'])
def index():
    return render_template("index.html")#fichier racine

#decorateur mode selection
@app.route('/selection', 
           methods=['GET'])
def selection():
    return render_template("selection.html")#fichier selection

#decorateur mode insertion
@app.route('/insertion',
            methods=['GET'])
def insertion():
    return render_template("insertion.html")#fichier insertion

#decorateur de reception de données
@app.route('/get', 
           methods=['POST'])
def get():
    #verification du mode choisi (insertion/selection)
    insertion = 'insertion' in request.form
    selection = 'selection' in request.form 

    liste = request.form.get('input', '')  # Récupère la chaîne sous forme de string
    liste = [int(x.strip()) for x in liste.split(',') if x.strip().isdigit()]  # Transforme en liste
    liste_encodée = urllib.parse.quote(json.dumps(liste), safe='')  # Encode correctement (avec json)

    #gestion des erreurs (2 cases cochées ou aucune)
    #le switch case ne marcherai pas ici meme avec output = (insertion,selection)
    if (insertion and selection) or (not insertion and not selection):
        flash("tu me prend pour un jambon?") #renvoie une alert
        return redirect(url_for('index'))    #redirection vers la main page

    if insertion:
        return redirect(url_for('insertion', 
                                valeur=liste_encodée))

    if selection:
        return redirect(url_for('selection', 
                                valeur=liste_encodée))


if __name__ == '__main__':#execution du script si le fichier est le principal (renvoie True)
    app.run(debug=True)
