


class person:

    legs =4

    def __init__(self,name, type):
        self.name = name
        self.type=type

    def about(self,details):
        self.details=details
        return details

    @classmethod
    def update_legs(cls,legs):
        cls.legs=legs
        return legs

    @classmethod
    def create_constructor_using_method(cls,str):

        return cls(*str.split("."))


    @staticmethod
    def newLegs(extra_legs):
        return extra_legs

ram = person.create_constructor_using_method("ram.boy")

print(ram.name)

print(ram.newLegs(5))
extra =ram.update_legs(67)
print(extra)
print(person.legs)
priya = person("priya","girl")
ranjan = person("ranjan","man")
a=priya.about("she is a good girl")
ar=ranjan.about("he is a good boy")

print(priya.name)
print(ranjan.type)
print(a)
print(ar)
print(priya.legs)