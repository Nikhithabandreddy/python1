l=['c','python','','','java','','']
nullcount=0
for i in l:
    if(i==''):
        nullcount+=1
print("Number of null values are:",nullcount)