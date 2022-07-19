a = input()
m=[]
for i in a:
    if i.isalnum():
        m.append(i)
n=0
m=sorted(m)
for i in a:
    if i.isalnum():
        print(m[n],end="")
        n+=1
    else:
        print(i,end="")
        
