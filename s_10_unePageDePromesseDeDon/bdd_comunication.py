import mysql.connector as mysqlpy

class Connexion_bdd:
    __USER = 'root'
    __PWD = 'example'
    __HOST = 'localhost'
    __PORT = '3307'
    __DB = 'don_pour_site_de_don'
    __bdd = None

    @classmethod
    def connexion(cls):
        cls.__bdd = mysqlpy.connect(user=cls.__USER, password=cls.__PWD, host=cls.__HOST, port=cls.__PORT, database=cls.__DB)
        return cls.__bdd.cursor()

    @classmethod
    def deconnexion(cls, commit=False):
        if cls.__bdd:
            if commit:
                cls.__bdd.commit()

            cls.__bdd.close()
            cls.__bdd = None