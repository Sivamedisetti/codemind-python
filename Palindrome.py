n=int(input())
a=n
s=0
while n:
    k=n%10
    s=s*10+k
    n=n//10
if a==s:
    print(True)
else:
    print(False)
    