n=int(input())
l=list(map(int,input().split()))
s=sorted(set(l),key=l.index)
print(*s)