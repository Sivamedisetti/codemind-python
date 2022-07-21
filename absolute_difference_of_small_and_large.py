l=list(map(str,input().split()))
n,m=[],[]
s,k=0,0
for i in l:
    n.append(max(i))
    m.append(min(i))
    for i in n:
        s+=ord(i)
    for i in m:
        k+=ord(i)
    print(abs(s-k),end=" ")
    m.clear()
    n.clear()
    s,k=0,0