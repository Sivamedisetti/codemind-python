def even(n):
    if n%2==0:
        return 1
    else:
        return 0
x = int(input())
l = list(map(int,input().split()))
sum=0
for i in l:
    if even(i):
        break
    else:
        sum+=i
print(sum)