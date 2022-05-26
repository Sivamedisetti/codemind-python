x=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
for i in range(x):
    if l[i]>=a and l[i]<=b:
        pass
    else:
        print(l[i],end=" ")
        c=1
if c==0:
    print("-1")