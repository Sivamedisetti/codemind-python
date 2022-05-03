a,b=0,1
n=int(input())
c=a+b
if n==0:
   print("True") 
while c<n:
    c=a+b
    a=b
    b=c
if n==c:
    print("True")
else:
    print("False")