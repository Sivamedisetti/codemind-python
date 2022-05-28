def prime(n):
    if n==1:
        return 0
    for i in range(2,(n//2)+1):
        if n%i==0:
            return 0
    return 1
x = int(input())
l = list(map(int,input().split()))
b=int(input())
c=0
for i in l:
    if i>=b:
        if prime(i):
            c+=1
print(c)
       