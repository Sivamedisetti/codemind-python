n=int(input())
for i in range(n):
    s=input()
    a=s[::-1]
    if s==a:
        if len(s)%2==0:
            print("YES EVEN")
        else:
             print("YES ODD")
    else:
        print("NO")