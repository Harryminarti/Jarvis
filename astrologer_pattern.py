

num = int(input("Enter your number to print the start\n"))
num1 = int(input("choose your decision 0 for false and 1 for true... \n"))

if num1==0:
 for j in range(0,num):
    for i in range(0,j+1):
        print("*",end="")
    print()
else:
 for j in range(0,num):
    for i in range(num,j,-1):
        print("*",end="")
    print()