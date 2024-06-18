
print("hello World")

class animal:

    roll_no=5

    def __init__(self,name):
        self.name = name

    def names(self):
        print(f"name of ths animal is: {self.name}")

    @property
    def roll_nos(self):
        return self.roll_no

    @roll_nos.setter
    def roll_nos(self,r):
        self.roll_no=r
        print(self.roll_no)



a1 = animal("dog")
a1.names()

a1.roll_nos=55
print(a1.roll_nos)