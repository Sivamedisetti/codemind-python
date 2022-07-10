n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    y=str(i)
    x=y[::-1]
    if i==int(x):
       c+=1
print(c)