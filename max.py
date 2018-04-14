n=int(input("enter a num"))
l=[]
for i in range(n):
    a=int(input("enter val"+str(i+1)))
    l.append(a)
for i in range(n):
    if i==4:
        break
    if(l[i]>l[i+1]):
        print(l[i])
    else:
        print(l[i+1])
