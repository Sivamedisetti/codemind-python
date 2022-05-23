def palin(n):
    k=n
    r=0
    while n:
        s=n%10
        r=r*10+s
        n//=10
    if k==r:
        return 1
    else:
        return 0
n=int(input())
k=n+1
#print(k)
for i in range(n-1,1,-1):
    if palin(i):
        a=i
        #print(a)
        break
while k!=0:
    if palin(k):
        b=k
        break
    k+=1
x=n-a
y=b-n
if x==y:
    print(a,b)
elif x>y:
    print(b)
else:
    print(a)