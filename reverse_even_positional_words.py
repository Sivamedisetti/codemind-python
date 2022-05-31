l=list(map(str,input().split()))
k=[]
for i in range(len(l)):
    if i%2==0:
        s=(l[i])[::-1]
        k.append(s)
    else:
        k.append(l[i])
print(*k)