def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return n
x=int(input())
for i in range(x):
    n=int(input())
    k=n
    for j in range(n,2,-1):
        if prime(j):
            a=j
            break
    while k!=0:
        if prime(k):
            b=k
            break
        k+=1
    if (n-a)<(b-n):
        print(a)
    elif (n-a)==(b-n):
        print(a)
    else:
        print(b)
    

            
        