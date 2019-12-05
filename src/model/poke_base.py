
import mysql.connector
from mysql.connector import Error


def get_trainers():
    try:
        connection = mysql.connector.connect(host='localhost', database='pokemon', user='root', password='Argenis616@')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT idTrainer,name FROM pokemon.Trainer;")
            s = ""
            trainers = cursor.fetchall()
            s += "0: Salir" + "\n"
            for t in trainers:
                s += str(t[0]) + ": " + str(t[1]) + "\n"
            return s
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            