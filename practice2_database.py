
import mysql.connector

mydb = mysql.connector.connect(host='localhost',user ='root',password ='1234',database='std_info')

curs = mydb.cursor()

# str1 = "update students_details set std_id = std_id+10 where std_id >2" ......update command

str2 = "delete from students_details where course='bba'"
curs.execute(str2)

mydb.commit()