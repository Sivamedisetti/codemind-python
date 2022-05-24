def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
c=[]
s=[]
for i in range(1,n+1,1):
    if n%i==0:
        if prime(i):
            c.append(i)
        else:
            s.append(i)
print(len(s))
    
        
