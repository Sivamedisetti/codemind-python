n=int(input())
l=list(map(int,input().split()))
x=[]
y=[]
for i in range(n):
    if l[i]%2==0:
        x.append(l[i])
    else:
        y.append(l[i])
i,j=0,0
while i<len(x) or j<len(y):
    if i<len(x):
        print(x[i],end=" ")
        i+=1
    if j<len(y):
        print(y[j],end=" ")
        j+=1
if n%2==1:
    print("0")