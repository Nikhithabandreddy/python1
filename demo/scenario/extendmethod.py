a=[1,2,3,4]
b=[4,5,6,7]
print(a)
print(b)
a.extend(b)
print(a)
b.extend(a)
print(b)
b.extend(b)
print(b)