def palin(n):
    k=n
    r=0
    while n!=0:
        s=n%10
        r=r*10+s
        n//=10
    if k==r:
        return 1
    else: 
        return 0
def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
while n!=0:
    n+=1
    if prime(n):
        if palin(n):
            print(n)
            break
    










