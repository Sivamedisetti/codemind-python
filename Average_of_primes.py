def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    if prime(i):
        k.append(i)
print(format(sum(k)/len(k),".2f"))