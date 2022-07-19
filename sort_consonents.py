l=list(map(str,input().split()))
m=[]
s="aeiouAEIOU"
for i in l:
    for j in i:
        if j not in s:
            m.append(j)
    m.sort()
    a=0
    for j in i:
        if j in s:
            print(j,end="")
        else:
            print(m[a],end="")
            a+=1
    print("",end=" ")
    m.clear()
