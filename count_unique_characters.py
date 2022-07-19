n=input()
s=0
for i in n:
    if i>='a'and i<='z':
        if n.count(i)==1:
            s+=1
print(s)