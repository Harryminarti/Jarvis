

class water_animal:
    swim=True
    var =9
    def __init__(self):
        print("this is called form water animal")

class earth_animal:
    legs =4
    var =5

    def __init__(self):
        print("this is call from earth animal")

class turtle(water_animal,earth_animal):
    var =4

    def fuc(self,name):
        self.name = name

t1 =turtle()
t1.fuc("turtles")
print(t1.name)
print(t1.var)

print(turtle.var)
t2 = turtle()

w1 = water_animal()

