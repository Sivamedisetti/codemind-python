n=int(input())
k=0
while n:
    s=n%10
    if s>=k:
        k=s
    n=n//10
print(k)