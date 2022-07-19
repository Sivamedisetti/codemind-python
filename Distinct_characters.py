n=input().lower()
m=sorted(set(n))
a=[]
for i in m:
    if i>='a'and i<='z':
        print(i,end="")