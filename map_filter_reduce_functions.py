

list1 =[1,2,3,5,6,6,8,0,9]

def sqr (a):
    return a*a

#map
a = list(map(sqr,list1))
print(a)

# filter

def greater_than(a):
    return a>5

b =list(filter(greater_than,list1))

print(b)

#reduce...

from functools import reduce

c = reduce(lambda x,y:x+y,list1)
print(c)