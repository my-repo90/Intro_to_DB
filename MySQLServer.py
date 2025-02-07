from configparser import ConfigParser
import mysql.connector

file = "config.ini" #   the file which contains the configuration infos
config = ConfigParser() #   creating a configparser object

config.read(file)

try:    
    mydb = mysql.connector.connect(
        host = config['DB_INFOS']['host'],
        user = config['DB_INFOS']['user'],
        password = config['DB_INFOS']['password']
    )
    mycursor = mydb.cursor()    #   creating the mycursor object

    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("'alx_book_store' database is created successfully")
    mycursor.execute("SHOW DATABASES")
    for i in mycursor:
        print(i)
except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))
