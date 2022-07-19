a = input().lower()
b = input().lower()
m,s,x=[],[],[]
for i in a:
    if i!=" ":
        m.append(i)
for i in b:
    if i!=" ":
        s.append(i)
for i in m:
    if i not in s:
        x.append(i)
for i in s:
    if i not in m:
        x.append(i)
x=sorted(set(x))
for i in x:
    print(i,end="")