
import mysql.connector

mydb = mysql.connector.connect(host='localhost',user='root',password='1234',database = 'std_info')
print(mydb.connection_id)

# str1 = "create database std_info"
# str2 = "create table students_details (std_id Integer(5),name varchar(20),course varchar(20))"

str3 = "insert into students_details (std_id,name,course) values(%s,%s,%s)"

# t1 =(1,"priya","btech")

# std_coll = [(2,"ranjan","bca"),(3,"ravi","bba"),(4,"priya Ranjan","Bca")]

curs =mydb.cursor()

# curs.executemany(str3,std_coll)

# data = "select * from students_details"
d1 = "select * from students_details where name ='priya'"
d2 = "select name from students_details where std_id =2"
curs.execute(d2)

details = curs.fetchall()

mydb.commit()

for i in details:
    print(i)


