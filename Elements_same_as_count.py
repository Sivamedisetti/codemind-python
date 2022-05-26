x = int(input())
l = list(map(int,input().split()))
c=0
for i in sorted(set(l),key=l.index):
    if l.count(i)==i:
        print(i,end=" ")
        c=1
if c==0:
    print("-1")