
def user_id():
    print("Choose your client by id :")
    print("Harry id=1")
    print("Ravi id =2")
    print("Rohan id=3")

    user_input = input('Enter user_id: ')
    if user_input=='1'or user_input=='2'or user_input=='3':
        return user_input
    else:
      print( "Id",user_input ,"is not exist")
      user_id()

# --------------------------------------------------------------------------

def



def retrieve():
    print("Hello World1")
    print(user_id())


def update():
    print("Hello World2")
    print(user_id())

# ----------------------------------------------------------------------------

print("Choose your options: ")
print("1. For Retrieve Client Data")
print("2. For Update Client Data")
print(" Any Button For Exist ")
print("------------------------------------------------")


user_option = input("Enter Your Choice: ")


if user_option=='1':
    retrieve()
elif user_option=='2':
    update()
else:
    print("You are exist from the program")
    exit()

