

print("Hello World")

d1 = {"rohan":"roti",
      "aman":"game",
      "amit":"ridhi"}

print(d1)

d1["priyaranjan"]="shivi"
print(d1)

d3 = d1
print(d3.get("aman"))
print(d3.update({"priyaranjan": "shivaksi"}))
print(d1)
d2=d1.copy();

del d2["aman"]
print(d2,d1)
d2.update({"pratham":"barksha"})
print(d2)