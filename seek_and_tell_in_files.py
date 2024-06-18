

f = open("intro2.txt")
print(f.tell())
val =f.read()
print(val)
print(f.tell())

f.seek(5)
print(f.tell())
print(f.read())
