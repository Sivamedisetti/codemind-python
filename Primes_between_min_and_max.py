def prime(n):
    if n==1:
        return 0
    for i in range(2,(n//2)+1):
        if n%i==0:
            return 0
    return 1
x = int(input())
l = list(map(int,input().split()))
a=l.index(max(l))
b=l.index(min(l))
c=0
if a>b:
    for i in range(b,a+1):
        if prime(l[i]):
            c+=1
else:
    for i in range(a,b+1):
        if prime(l[i]):
            c+=1
print(c)
 