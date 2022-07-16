n=list(map(str,input().split()))
s=[]
k=0
for i in n:
    for j in i:
        k+=ord(j)
    s.append([k,i])
    k=0
s.sort()
for i in s:
    print(i[1],end=" ")

