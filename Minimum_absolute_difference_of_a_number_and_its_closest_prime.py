def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
k=n
for i in range(n,2,-1):
    if prime(i):
        a=i
        break
while k!=0:
    if prime(k):
        b=k
        break
    k+=1
x=n-a
y=b-n
#if prime(a):
 #   print(a)
if x>y:
    print(y)
else:
    print(x)
    
        
