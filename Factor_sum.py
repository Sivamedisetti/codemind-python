l=list(map(int,input().split(',')))
f=0
for i in set(l):
    p=0
    s=0
    for j in range(1,i+1):
        if i%j==0:
            s+=j
    for k in l:
        if k==s:
            p=1
    if p==1:
        print(i,end=" ")
        f=1
if f==0:
    print("-1")