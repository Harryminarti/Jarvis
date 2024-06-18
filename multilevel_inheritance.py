
class dad:

    basketball =1

    def __init__(self,name):
        self.name = name


    def val(self,basketballs):
        self.basketball = basketballs


class son(dad):
    cricket =2
    def change_cricket(self):
        print(f"this is the self dance is :{self.cricket}")


class grandson(son):

    cricket = 5

    def __int__(self):
        print("this is the grandson")
    #
    # def change_cricket(self):
    #     print(f"for the schsi os{self.cricket}")


d1 = grandson("raja")
d3 = son("rohan")
d3.change_cricket()

d1.change_cricket()


