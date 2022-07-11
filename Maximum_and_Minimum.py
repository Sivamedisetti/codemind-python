n=int(input())
l=list(map(int,input().split()))
m=[]
for i in set(l):
    if i==l.count(i):
        m.append(i)
if m==[]:
    print("-1")
else:
    print(min(m),end=" ")
    print(max(m),end=" ")
    