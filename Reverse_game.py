def palli(n):
   r=0
   while n!=0:
       s=n%10
       r=r*10+s
       n//=10
   return r
n=int(input())
l=list(map(int,input().split()))
for i in l:
    print(palli(i),end=" ")
        