

def details(person):
    def p1(*ars,**kwargs):
        print("helo good morning")
        person(*ars,**kwargs)

    return p1

@details
def person(name,age):
    print(f"name of the p1 is {name} and age is {age}")

p12=person("harry",21)

