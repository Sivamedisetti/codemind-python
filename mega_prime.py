def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
k=n
c,a=0,0
if prime(n):
    while n!=0:
        s=n%10
        if prime(s):
            c+=1
        n=n//10
        if c==len(str(k)):
            a=1   
    if a==1:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")
    
        