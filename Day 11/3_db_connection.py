import mysql.connector # pip install mysql-connector

mydb = mysql.connector.connect(host="localhost",user="root",password="root")

mycurser = mydb.cursor()

mycurser.execute("show databases")

for i in mycurser:
    print(i)