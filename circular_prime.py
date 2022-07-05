def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1,1):
        if n%i==0:
            return 0
    return 1
n=int(input())
if prime(n):
    x=str(n)
    y=x[::-1]
    if prime(int(y)):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")
        