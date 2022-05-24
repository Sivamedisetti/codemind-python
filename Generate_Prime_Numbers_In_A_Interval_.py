def prime(n):                             
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return(False)
    else:
        return(True)
x= int(input())
y=int(input())
for i in range(x+1,y):
    if prime(i):
        print(i)