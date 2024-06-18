

class father:

    def __init__(self,name ,age):
        self.name = name
        self.age = age

    def details(self):
        print(f"Name of father is: {self.name} and his age is : {self.age}")



class son(father):

    def __init__(self,name ,age):
        self.name =name
        self.age =age

    # def details(self):
    #     print(f"Name of son is: {self.name} and his age is : {self.age}")


    def details_son(self):
        print(f"This is the details of son:\n"
              f" name is : {self.name},age is:{self.age} ,sport: ")


f1 = father ("harry",22)
f1.details()
print()

s1 = son("rowdy",25)
s1.details_son()
s1.details()