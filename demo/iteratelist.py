proglang=['c','cpp','python','java','php']
print(proglang)
print(type(proglang))
print("------------")
#iterating list elements without index
for i in proglang:
    print(i)
print("---------------")
#iterating list elemnts with index
for i in range(len(proglang)):
    print(proglang[i])
print("---------------")
#iterating list elemnts using while
i=0
n=len(proglang)
while i<n:
    print(proglang[i])
    i+=1