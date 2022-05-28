a,b=map(int,input().split())
l = list(map(int,input().split()))
m = list(map(int,input().split()))
c=0
for i in set(l):
    if i in set(m):
        c+=1
for j in (set(m)):
    if j in set(l)==0:
        c+=1
print(c)