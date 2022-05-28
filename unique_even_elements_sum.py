n=int(input())
l=list(map(int,input().split()))
sum=0
for i in set(l):
    if i%2==0:
        sum+=i
print(sum)