

# list =[1,2,3,5]
# for item in list:
#     print(item)
#
# l1 = [[1,2],[3,4],[5,6]]
#
# for item,value in l1:
#     print(item,value)
#
# d1 = dict(l1)
#
#
# for item,value in d1.items():
#     print(item, value)

l2 =[1,2,4,str,"float",int,float,"priyaranjan",8,9]

for item in l2 :
    if str(item).isnumeric() and item>5:
        print(item)
