n=int(input())
l=list(map(int,input().split()))
a,b=0,0
for i in range(n):
    if i<n//2:
        a+=l[i]
    else:
        b+=l[i]
print(a)
print(b)