
class person:
    name=''
    roll=None
    age=int


    def __init__(self,classes ,roll):

        self.classes=classes
        self.roll=roll

    def age(self,name,age):
        self.name =name
        self.age =age
        return age

rohan = person("4",22)

print(rohan.age)
print(rohan.name)

print(rohan.age("ranjan",33))
print(rohan.name)
print(rohan.classes)
print(rohan.roll)
print(person.name)

print(person.age,person.name)