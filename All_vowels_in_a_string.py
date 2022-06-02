n=input()
a=[]
b=[]
for i in n:
    if i=='a'or i=='e'or i=='i'or i=='o' or i =='u':
        a.append(i)
    elif i=='A'or i=='E'or i=='I'or i=='O' or i =='U':
        b.append(i)
m=len(set(a))
n=len(set(b))
if m==5:
    print(True)
elif n==5:
    print(True)
else:
    print(False)
    
