n=int(input())
a=0
for i in range(1,n+1):
    s=1/i
    a+=s
print(format(a,".2f"))