n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(1,n-1,2):
    if l[i-1]>l[i]<l[i+1] or l[i-1]<l[i]>l[i+1]:
        c+=1
    else:
        print("no")
        c=0
        break
if c!=0:
    print("yes")