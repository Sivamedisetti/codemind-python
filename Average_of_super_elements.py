n=int(input())
l=list(map(int,input().split()))
c=[]
for i in set(l):
    if i==l.count(i):
        c.append(i)
if c==[]:
    print("-1")
else:
    print(format(sum(c)/len(c),".2f"))
