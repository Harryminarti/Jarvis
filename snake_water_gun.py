

import random

l1 = ["s","w","g"]
print("for snake enter s and for water enter w and for gun enter g")

i =0
comp_win=0
you_win =0

while i <10:
    user_input = input("Enter your val")

    if(random.choice(l1)=='s' and user_input=='g'):
        print("you win")
        you_win+=1
    elif (random.choice(l1)=='w' and user_input=='s'):
        print("you win")
        you_win+=1
    elif(random.choice(l1)=='g' and user_input=='w'):
        print("You win")
        you_win+=1
    else:
        print("computer win")
        comp_win+=1
    i+=1

print("total score is : ")
print("You win: ",you_win)
print("computer win:",comp_win)