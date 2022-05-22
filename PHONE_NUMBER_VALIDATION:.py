n=int(input())
c=0
while n:
    s=n%10
    if s>=0:
        c+=1
    n=n//10
if c==10:
    print('Valid')
else:
    print('Invalid')