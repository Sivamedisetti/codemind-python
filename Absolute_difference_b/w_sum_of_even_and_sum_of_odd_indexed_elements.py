x=int(input())
l=list(map(int,input().split()))
a,b=0,0
for i in range(len(l)):
    if i%2==0:
        a+=l[i]
    else:
        b+=l[i]
print(abs(b-a))
    



