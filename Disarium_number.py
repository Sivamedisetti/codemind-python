x=eval(input())
a=x
n=len(str(x))
s=0
while x!=0:
    y=x%10
    x=x//10
    m=y**n
    s+=m
    n-=1
if s==a:
    print("True")
else:
    print("False")
    