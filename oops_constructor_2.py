

class animal:
    def types(self):
        print("this is the simple method ")
        
    def __init__(self,breed,age):
        self.breed = breed
        self.age = age

a1 = animal("dogs",22)
print(a1.age,a1.breed)
a1.types()