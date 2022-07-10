n=int(input())
l=list(map(int,input().split()))
m=[]
for i in l:
    m.append(len(str(i)))
x=min(m)
c=0
for i in m:
    if i<=x:
        c+=1
print(c)