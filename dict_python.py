import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
    database ='t1'
)

cursors = mydb.cursor()
# cursors.execute("create database if not exists t1")

val ="insert into t1 (name,address)values(%s,%s)"

t1 =(input(),input())

cursors.execute(val,t1)
mydb.commit()
mydb.close()
cursors.close()