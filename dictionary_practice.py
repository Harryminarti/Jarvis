
"""
1. Make a dictionary in which have a meanings of the word given and match the input of user and gives the result of
input or meaning of the user input ..... user input is already exist in dictionary (given in question)...

"""

d1 = {
    "first_name": "It is the first users starting name symbols ",
    "last_name": "it is the mainly user title to denote its roots personality",
    "dob": "it is a day in which user is born",
    "user_id": "it is the unique identification of user without revealing their data",
    "user_name": " it is the professional name of the users"
}
print("  ",end='')
val = input("Enter your value get meaning of that value  of the data")

print(d1[val])