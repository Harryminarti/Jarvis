
class  animal:
    def __init__(self,name):
        self.name = name

    def legs(self,No_of_legs):
        self.No_of_legs =No_of_legs
        return No_of_legs


class dog(animal):
    pass

d1 = dog("tommy")
print(d1.name)
print(d1.legs(5))
print(d1.No_of_legs)