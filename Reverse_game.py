n=int(input())
l=list(map(int,input().split()))
for i in l:
    c=0
    while i!=0:
        x=i%10
        c=c*10+x
        i//=10
    print(c,end=" ")