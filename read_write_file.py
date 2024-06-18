
#creating the file through write mode........

# f=open("intro2.txt","w")
# f.close()

#reading and write in file through by using r+
#
# f =open("intro2.txt","r+")
#
#
# content = f.read()
# print(content)
# f.close()

f = open("intro2.txt","r+")

f.write("i hope you shall enjoy it in lyour world oth the \n")
print(f.read())