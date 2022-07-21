n=input()
m=[]
for i in n:
    if i.isalpha():
        m.append(i)
print(min(m),m.count(min(m)),max(m),m.count(max(m)))
