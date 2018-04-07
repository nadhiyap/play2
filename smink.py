a=int(input("enter number"))
k=int(input("enter number"))
l=[]
for i in range(a):
    b=int(input("enter number"))
    l.append(b)
for i in range(k-1):
    b=min(l)
    l.remove(b)
print(min(l))
    
