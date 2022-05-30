def dig(n):
    c=0
    if n==0:
        return 1
    if n<0:
        n=-1*n
    while n!=0:
        s=n%10
        c+=1
        n//=10
    return c
n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n):
    print(dig(l[i]),end=" ")