

class animal:

    def details(self):
        print(f"name of animal is {self.name} and age is {self.age}")

    def name(self,n):
        self.name =n

    def __init__(self):
        self.age = 22

    @property
    def age_value(self):
        return 10*self.age

    @age_value.setter
    def age_value(self,new_age):
        self.age = new_age


a1 = animal()

a1.details()

a1.age_value=44
print(a1.age_value)

