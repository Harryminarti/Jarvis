

numb = 88
count=10


while count>0:
    user_input = int(input("Enter your numbers..."))

    if(user_input<=50):
        print("Your guessing is tooo low")
    elif(user_input>50  and user_input<88):
        print("you nedd increasing your number")
    elif(user_input>88):
        print("You need to decrease your number")
    else:
        print("you won , you find the numbers...")
        break;

    count=count-1
    print("Only ",count,"chances is left")
