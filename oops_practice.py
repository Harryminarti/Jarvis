

class person:
    name = "harry"
    age=20

    def details(self):
        print(f"name of the person is {self.name} and age is {self.age}")

    def __init__(self,name,age):
        self.name = name
        self.age = age


p1 = person("Harry",22)
print(p1.name)
print(p1.age)

p1.details()

p2 = person("priya",23)
p2.details()