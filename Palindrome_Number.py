x=eval(input())
for  i in range(x):
    n=int(input())
    s=0
    m=n
    while n!=0:
        k=n%10
        s=s*10+k
        n = n//10
        #print(s)
    if m==s:
        print(True)
    else:
        print(False)
        