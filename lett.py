a=input("enter string")
b=input("enter string")
c=1
for letter in a: 
    if letter in b:
        c=0
        break
if(c==0):
    print("yes")
else:
    print("no")
    
