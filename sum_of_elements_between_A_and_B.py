n=input()
l=list(map(int,input().split()))
m=[]
x,y=map(int,input().split())
c=0
for i in l:
    if i>=x and i<=y:
        m.append(i)
        c=1
if c==0:
    print("-1")
print(sum(m))