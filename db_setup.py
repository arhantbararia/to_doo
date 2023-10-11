from dotenv import load_dotenv
import os
import mysql.connector



load_dotenv()
MYSQL_HOST =  os.environ.get("MYSQL_HOST")
MYSQL_USER = os.environ.get("MYSQL_USER")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")




dataBase = mysql.connector.connect(
    host= MYSQL_HOST,
    user= MYSQL_USER,
    passwd = MYSQL_PASSWORD,

)



cursor = dataBase.cursor()

cursor.execute("CREATE DATABASE To_do_Data")

print("DATABASE created!")