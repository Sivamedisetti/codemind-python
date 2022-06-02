n=input()
c=0
for i in sorted(set(n),key=n.index):
    if i in 'AEIOUaeiou':
        print(i,end=' ')
        c=1
if c==0:
    print("-1")