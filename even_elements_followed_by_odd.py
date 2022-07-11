n=int(input())
l=list(map(int,input().split()))
m=[]
for i in l:
    if i%2==1:
        m.append(i)
    else:
        print(i,end=" ")
print(*m)