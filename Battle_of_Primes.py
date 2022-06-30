def prime(n):
    if n==1:
        return 0
    for i in range(2,(n//2)+1):
        if n%i==0:
            return 0
    else:
        return 1
x=int(input())
y=int(input())
a=x+y+1
while a!=0:
    if prime(a):
        print(abs(x+y-a))
        break
    a+=1