#write mode..

f = open("introduction.txt","w")
len =f.write("hiii, this is me priya ranjan trying to write in the file\n")
f.close()
print(len)

#append mode

d = open("introduction.txt","a")
len =d.write("trying to append some of the character in the file\n")

print(len)
