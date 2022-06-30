def prime(n):
    if n==1:
        return 0
    for i in range(2,(n//2)+1):
        if n%i==0:
            return 0
            break
    return 1
x = int(input())
c=0
for i in range(1,x+1):
    if x%i==0:
        if prime(i):
            pass
        else:
            c+=1
print(c)