

print("hello World")


str1 = "hello "
str2 ="%sworld "%str1

print("this is the",str2)

str3 = "this is the{1}{0}"

str4 = str3.format(str1,str2)

print(str4)
print(f"this is not same brothrer {str4}{str3} {str2}")