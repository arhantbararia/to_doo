
import mysql.connector


dataBase = mysql.connector.connect(
    host= 'localhost',
    user= 'arhantbararia',
    passwd = 'arh123',

)



cursor = dataBase.cursor()

cursor.execute("CREATE DATABASE To_do_Data")

print("DATABASE created!")