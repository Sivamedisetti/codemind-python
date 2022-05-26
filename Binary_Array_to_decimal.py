n=int(input())
l=list(map(int,input().split()))
j=0
r=0
for i in range(n-1,-1,-1):
    r=r+l[i]*(2**j)
    j+=1
print(r)
    

