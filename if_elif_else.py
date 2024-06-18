
age = int(input("Enter your age"))
print()

if age<18 and age>4:
    print("You can't drive , your age is lower than expected")
elif age==18:
    print("first your need give physical test, then we can decide")
elif age>18 and age<100:
    print("Yes , you can drive")


else:
    print("You are not capable to drive")

l1 = [1,2,3,5]

if 5 in l1:
    print("Yes, it is found in the lists")