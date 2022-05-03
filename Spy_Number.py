s=0
p=1
n=int(input())
while n!=0:
    x=n%10
    n=n//10
    s+=x
    p*=x
if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")
