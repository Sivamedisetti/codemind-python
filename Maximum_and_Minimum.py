x = int(input())
l = list(map(int,input().split()))
s=[]
c=0
for i in set(l):
    if l.count(i)==i:
        s.append(i)
if s==[]:
    print("-1")
else:
    print(min(s),end=" ")
    print(max(s))