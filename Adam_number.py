def rev(n):
    r=0
    while n:
        s=n%10
        r=r*10+s
        n//=10
    return r
n=int(input())
x=rev(n)
y=x**2
z=rev(y)
if n**2==z:
    print(True)
else:
    print(False)
