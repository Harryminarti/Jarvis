import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', password='1234',database='db1')
print(mydb.connection_id)

cursors = mydb.cursor()
# cursors.execute("create database db1") ---------database is created
# cursors.execute("create table book(bookid integer(5), title varchar (20), price float(5,4))")----table is created

str = "insert into book (bookid,title,price) values (%s,%s,%s)"
book_info = (1,"python book",595.44)

cursors.execute(str,book_info)

mydb.commit()
