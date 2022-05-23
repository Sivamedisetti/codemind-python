x = int(input())
for i in range(x):
    n,m = map(int,input().split())
    for j in range(m+1):
        if (j**2)%m==n:
            print(j)
            break
    else:
        print('-1')