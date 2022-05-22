n=int(input())
k=n
r=0
while n:
    s=n%10
    r+=s
    n=n//10
if k%r==0:
    print(True)
else:
    print(False)
    
