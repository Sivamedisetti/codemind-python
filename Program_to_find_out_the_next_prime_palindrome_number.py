def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1,1):
        if n%i==0:
            return 0
    return 1
x=int(input())
y=x+1
while True:
    if prime(y):
        n=str(y)
        a=n[::-1]
        if n==a:
            print(n)
            break
    y+=1
