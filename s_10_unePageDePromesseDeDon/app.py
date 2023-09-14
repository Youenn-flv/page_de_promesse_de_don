from flask import Flask, render_template, request, redirect, url_for
from data import DonReusuData

app = Flask(__name__)

@app.route('/')
def index():
    titre = "page de donnation"
    contenu = "voulez vous nous faire un don ?"
    return render_template('index.html', titre=titre, contenu=contenu)

@app.route('/formulaire')
def formulaire():
    return render_template('formulaire.html')

@app.route('/remerciment')
def remerciment():
    return render_template('remerciment.html')

@app.route('/soumettre_dons', methods=['POST'])
def soumettre_dons():
    nom = request.form.get('nom')
    prenom = request.form.get('prenom')
    email = request.form.get('email')
    montant = request.form.get('montant')
    devise = request.form.get('devise')

    DonReusuData.send_data_to_bdd(nom, prenom, email, montant, devise)

    return redirect(url_for('remerciment'))

if __name__ == '__main__':
    app.run(debug=True)
