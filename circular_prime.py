def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
s=0
if prime(n):
    while n:
        k=n%10
        s=(s*10)+k
        n=n//10
    if prime(s):
        print("circular prime")
    elif prime(n):
        print("prime but not a circular prime")
else:
    print("not prime")