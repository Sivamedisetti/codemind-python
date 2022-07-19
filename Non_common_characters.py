a = input().lower()
b = input().lower()
m,s,x=[],[],[]
for i in a:
    if i.isalpha():
        m.append(i)
for i in b:
    if i.isalpha():
        s.append(i)
for i in m:
    if i not in s:
        x.append(i)
for i in s:
    if i not in m:
        x.append(i)
x=sorted(set(x))
print(len(x))
    