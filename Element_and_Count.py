n=int(input())
l=list(map(int,input().split()))
x=[]
y=[]
for i in sorted(set(l),key=l.index):
    print(i,l.count(i),end=" ")
