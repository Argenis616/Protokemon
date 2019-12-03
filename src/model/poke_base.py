
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost', database='pokemon', user='root', password='root')
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("SELECT idTrainer,name FROM pokemon.Trainer;")
        for row in cursor:
            print row
        
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()