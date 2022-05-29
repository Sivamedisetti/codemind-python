n=int(input())
l=list(map(int,input().split()))
c=1
for i in range(1,n-1,2):
    if l[i-1]>l[i]<l[i+1] or l[i-1]<l[i]>l[i+1]:
        pass
    else:
        c=0
        break
if c==0:
    print("no")
else:
    print("yes")
    