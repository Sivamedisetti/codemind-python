n=int(input())
l=list(map(int,input().split()))
k=sum(l)//len(l)
if k in l:
    print(True)
else:
    print(False)