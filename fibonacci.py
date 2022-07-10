def fib(x):
    a = 0
    b = 1
    if x==0:
        return 1
    c = a+b
    while c<x:
        c = a + b
        a = b 
        b = c
    if x==c:
        return 1
    else:
        return 0
n=int(input())
print("0 1",end=" ")
c=3
i=1
while(1):
    if fib(i):
        print(i,end=" ")
        c+=1
        if c>n:
            break
    i+=1
    
    