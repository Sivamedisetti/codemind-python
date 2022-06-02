n=input()
c=0
s=0
for i in n:
    if i in "aeiouAEIOU":
        c+=1
        s=1
if s==0:
    print("0")
else:
    print(c)
    