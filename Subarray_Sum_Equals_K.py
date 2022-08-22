n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
s=0
for i in range(n):
    for j in range(i,n):
        s+=l[j]
        if s==k:
            c+=1
        if s>k:
            break
    s=0
print(c)
    