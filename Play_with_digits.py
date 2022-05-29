def sum(n):
    sum=0
    while n!=0:
        s=n%10
        sum+=s
        n//=10
    return sum
n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    c+=sum(i)
print(c)
        