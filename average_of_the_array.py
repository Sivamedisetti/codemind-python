x=int(input())
sum=0
l=list(map(int,input().split()))
for i in l:
    sum+=i
a=sum/x
print(format(a,".2f"))