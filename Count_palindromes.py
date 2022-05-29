def palli(n):
   k=str(n)
   p=k[::-1]
   if p==k:
       return 1
n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if palli(i):
        c+=1
print(c)
        