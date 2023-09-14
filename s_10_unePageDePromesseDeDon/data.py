from bdd_comunication import Connexion_bdd

class DonReusuData:

    @staticmethod
    def convertir_devise(devise):
        taux_de_change = {
            '€': "euro",
            '$': "dolard",
            '¥': "yen"
        }
        return taux_de_change.get(devise, "rouble")


    @staticmethod
    def send_data_to_bdd(nom, prenom, email, montant, devise):
        try:
            cursor = Connexion_bdd.connexion()

            insert_query = "INSERT INTO don_reusu (nom, prenom, email, montant, devise) VALUES (%s, %s, %s, %s, %s)"
            data = (nom, prenom, email, montant, devise)
            cursor.execute(insert_query, data)

            Connexion_bdd.deconnexion(commit=True)
            print("Don inséré avec succès !")

        except Exception as e:
            print("Erreur lors de l'insertion du don :", e)

        

