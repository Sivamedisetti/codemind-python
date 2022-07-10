n,k=map(int,input().split())
l=list(map(int,input().split()))
m=[]
for i in l:
    m.append(len(str(abs(i))))
c=0
for i in m:
    if i==k:
        c+=1
print(c)