x=int(input())
l=list(map(int,input().split()))
s=[]
for i in set(l):
    if l.count(i)==i:
        s.append(i)
if s==[]:
    print("-1")
else:
    print(format(sum(s)/len(s),".2f"))
