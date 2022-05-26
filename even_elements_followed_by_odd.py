x=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    if i%2==0:
        print(i,end=" ")
    else:
        k.append(i)
print(*k)
