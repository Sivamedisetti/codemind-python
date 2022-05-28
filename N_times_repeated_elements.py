n=int(input())
l=list(map(int,input().split()))
s=int(input())
c=0
for i in set(l):
    if l.count(i)==s:
        print(i,end=" ")
        c=1
if c==0:
    print("-1")