

s = set()
s.add(1)
s.add(2)
s.add(2)
print(s)

# print(s.remove(1))
print(s)

s1 = {5,6}
s2 = s.union(s1)

print(s2)
print(s1.isdisjoint(s))
print(min(s))
print(max(s2))
print(len(s2))