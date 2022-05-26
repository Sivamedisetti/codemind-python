x=int(input())
sum=0
l=list(map(int,input().split()))
for i in range(len(l)):
    if i%2!=0:
        sum+=l[i]
print(sum)