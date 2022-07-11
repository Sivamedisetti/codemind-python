n=int(input())
l=list(map(int,input().split()))
m=[]
for i in sorted(set(l),key=l.index):
    if i==l.count(i):
        m.append(i)
if m==[]:
    print("-1")
else:
    print(*m)
    