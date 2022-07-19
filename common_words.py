a=list(map(str,input().lower().split()))
b=list(map(str,input().lower().split()))
l=[]
m=[]
for i in a:
    if i in b:
        l.append(i)
for i in b:
    if i in a:
        m.append(i)
for i in m:
    if i in l:
        print(i,end=" ")
        
        