def dig(n):
    c=0
    while n!=0:
        n//=10
        c+=1
    return c
n=int(input())
k=[]
l=list(map(int,input().split()))
for i in l:
    k.append(dig(i))
s=max(k)
print(k.count(s))
    