n=int(input())
l=list(map(int,input().split()))
s,c=0,0
for i in range(n):
    if i<n//2:
        s+=l[i]
    else:
        c+=l[i]
print(abs(c-s))