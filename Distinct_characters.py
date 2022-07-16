n=input()
s=[]
m=n.lower()
for i in n:
    if m.count(i)==1:
        s.append(i)
a=sorted(s)
for i in a:
    if i>='a'and i<='z':
        print(i,end="")