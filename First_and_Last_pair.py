#1 2 3 4
#5 6 7 
#1 7 2 6 3 5 4 0
n=int(input())
l=list(map(int,input().split()))
x=[]
y=[]
for i in range(n):
    if i<=n//2:
        x.append(l[i])
    else:
        y.append(l[i])
i,j=0,len(y)-1
while i<len(x) or j>=0:
    if i<len(x):
        print(x[i],end=" ")
        i+=1
    if j>=0:
        print(y[j],end=" ")
        j-=1
if n%2==1:
    print("0")