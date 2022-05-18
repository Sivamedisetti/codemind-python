def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
if prime(n):
    print("prime")
else:
    print("not a prime")
