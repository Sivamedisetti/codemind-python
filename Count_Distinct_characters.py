n=input().lower()
m=set(n)
s=0
for i in m:
    if i>="a" and i<="z":
            s+=1
print(s)