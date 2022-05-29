n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(1,n):
    if l[i-1]>l[i]:
        pass
    else:
        print("no")
        c=1
        break
if c==0:
    print("yes")