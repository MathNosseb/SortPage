from flask import Flask, render_template, redirect, url_for, request
import json
import urllib.parse
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/selection', methods=['GET'])
def selection():
    return render_template("selection.html")
@app.route('/insertion', methods=['GET'])
def insertion():
    return render_template("insertion.html")

@app.route('/recuperer', methods=['POST'])
def recuperer():
    insertion = 'insertion' in request.form  # Vérifie si coché
    selection = 'selection' in request.form  # Vérifie si coché

    # Convertir l'input en une liste propre
    liste = request.form.get('input', '')
    liste = [int(x.strip()) for x in liste.split(',') if x.strip().isdigit()]  # Convertit "1,2,3" en [1,2,3]

    liste = request.form.get('input', '')  # Récupère la chaîne "1,2"
    liste = [int(x.strip()) for x in liste.split(',') if x.strip().isdigit()]  # Transforme en [1, 2]
    liste_encodée = urllib.parse.quote(json.dumps(liste), safe='')  # Encode correctement


    if (insertion and selection) or (not insertion and not selection):
        return redirect(url_for('index'))

    if insertion:
        return redirect(url_for('insertion', valeur=liste_encodée))

    if selection:
        return redirect(url_for('selection', valeur=liste_encodée))


if __name__ == '__main__':
    app.run(debug=True)
