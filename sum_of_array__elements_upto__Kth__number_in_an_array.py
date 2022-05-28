x = int(input())
l = list(map(int,input().split()))
a=int(input())
k=[]
for i in range(x):
    if i<a:
        k.append(l[i])
if k==[]:
    print('-1')
else:
    print(sum(k))