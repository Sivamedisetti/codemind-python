l=list(map(str,input().split()))
m=[]
for i in l:
    for j in i:
        if j>='a' and j<='z':
            m.append(j)
    m.sort()
    a=0
    for j in i:
        if j>='a'and j<='z':
            print(m[a],end="")
            a+=1
        else:
            print(j,end="")
    print(end=" ")
    m.clear()
            
            