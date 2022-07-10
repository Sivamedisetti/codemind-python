n=int(input())
l=list(map(int,input().split()))
m=[]
for i in l:
    m.append(len(str(i)))
x=max(m)
c=0
for i in range(n):
    if m[i]==x:
        print(l[i],end=" ")