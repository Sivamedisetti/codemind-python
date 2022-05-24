def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input())
k=n
sum=0
while n!=0:
    s=n%10
    sum+=fact(s)
    n=n//10
if k==sum:
    print("The number",k,"is a strong number")
else:
    print("The number",k,"is not a strong number")