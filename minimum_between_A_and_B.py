n=int(input())
l=list(map(int,input().split()))
x=[]
f=0
a,b=map(int,input().split())
for i in l:
    if i>=a and i<=b:
        x.append(i)
        f=1
if f==0:
    print("-1")
else:
    print(min(x))