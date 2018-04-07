a=int(input("enter number"))
l=[]
for i in range(a):
    b=int(input("enter number"))
    l.append(b)
b=min(l)
l.remove(b)
print(min(l))
    
