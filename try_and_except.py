

"""Here we are gonna to use try and except keyword"""

num1 = input("Enter Your first numeber\n")
num2 = input("Enter Your second number\n")

try:
    print(int(num1)+int(num2))
except Exception as e:
    print(e)

print("This line is very important for our programs")