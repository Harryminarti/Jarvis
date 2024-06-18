# Declare the base class employee
class employee:
    # Constructor
    def __init__(self, number, name, designation, address, phone):
        self.number = number
        self.name = name
        self.designation = designation
        self.address = address
        self.phone = phone

    # Method to get data from user
    def getdata(self):
        self.number = input("Enter employee number: ")
        self.name = input("Enter employee name: ")
        self.designation = input("Enter employee designation: ")
        self.address = input("Enter employee address: ")
        self.phone = input("Enter employee phone number: ")

    # Method to display data
    def putdata(self):
        print("Employee number:", self.number)
        print("Employee name:", self.name)
        print("Employee designation:", self.designation)
        print("Employee address:", self.address)
        print("Employee phone number:", self.phone)


# Declare the derived class salary
class salary(employee):
    # Constructor
    def __init__(self, number, name, designation, address, phone, basic, da, hra, pf, tax):
        # Call the base class constructor
        employee.__init__(self, number, name, designation, address, phone)
        self.basic = basic
        self.da = da
        self.hra = hra
        self.pf = pf
        self.tax = tax
        self.gross = 0
        self.net = 0

    # Method to get data from user
    def getdata(self):
        # Call the base class method
        employee.getdata(self)
        self.basic = float(input("Enter basic pay: "))

    # Method to calculate gross and net pay
    def calculate(self):
        self.da = self.basic * 0.1  # 10% of basic pay
        self.hra = self.basic * 0.05  # 5% of basic pay
        self.gross = self.basic + self.da + self.hra
        self.pf = self.gross * 0.12  # 12% of gross pay
        self.tax = self.gross * 0.1  # 10% of gross pay
        self.net = self.gross - self.pf - self.tax

    # Method to display salary details
    def display(self):
        # Call the base class method
        employee.putdata(self)
        print("Basic pay:", self.basic)
        print("DA:", self.da)
        print("HRA:", self.hra)
        print("Gross pay:", self.gross)
        print("PF:", self.pf)
        print("Income tax:", self.tax)
        print("Net pay:", self.net)


# Create an object of the derived class
emp = salary(0, "", "", "", "", 0, 0, 0, 0, 0)
# Get the data from user
emp.getdata()
# Calculate the salary details
emp.calculate()
# Display the data
emp.display()
print("Created by: Aman Kumar")