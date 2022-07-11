n=int(input())
l=list(map(int,input().split()))
x,y=map(int,input().split())
m=[]
for i in l:
    if (i<x or i>y):
        m.append(i)
if m==[]:
    print("-1")
else:
    print(min(m))