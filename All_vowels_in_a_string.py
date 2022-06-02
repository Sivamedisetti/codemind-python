n=input()
a=[]
b=[]
for i in n:
    if i in "aeiou":
        a.append(i)
    elif i in "AEIOU":
        b.append(i)
m=len(set(a))
n=len(set(b))
if m==5:
    print(True)
elif n==5:
    print(True)
else:
    print(False)
    