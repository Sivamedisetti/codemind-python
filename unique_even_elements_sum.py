n=int(input())
l=set(map(int,input().split()))
c=0
for i in list(l):
    if i%2==0:
        c+=i
print(c)