x=int(input())
l=list(map(int,input().split()))
s=int(input())
for i in l:
    if s in l:
        print(True)
        break
    else:
        print(False)
        break