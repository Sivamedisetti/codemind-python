s=0
n=int(input())
x=n*n
p=s
while x!=0:
   y=x%10
   x=x//10
   s+=y
if n==s:
    print("Neon Number")
else:
    print("Not Neon Number")