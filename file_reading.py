
f = open("introduction.txt","r")
# content = f.read()
# print(content)
print(f.readlines())

for t in f:
    print(t)
print("---------------------------------")
print(f.readline())
print(f.readline())

f.close()