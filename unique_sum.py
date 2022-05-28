n=int(input())
l=list(map(int,input().split()))
sum=0
for i in set(l):
    sum+=i
print(sum)