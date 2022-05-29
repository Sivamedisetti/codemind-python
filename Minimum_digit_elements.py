def dig(n):
    c=0
    while n!=0:
        n//=10
        c+=1
    return c
n=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    k.append(dig(i))
s=min(k)
print(k.count(s))
