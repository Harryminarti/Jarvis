
import mysql.connector

mydb = mysql.connector.connect(host='localhost',user='priya',password ='admin')
print(mydb.connection_id)
mydb.close()