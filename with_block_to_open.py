

with open("intro2.txt")as f:
    print(f.read(40))#here is not need to close the file...by using of with open();

fs = open("intro2.txt","r+")
val = fs.read()
fs.write("ilkks ")
print(fs.read())
print(val)
f.close()