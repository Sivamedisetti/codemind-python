n=input()
s,c=0,0
for i in n:
    if i=="z":
        c+=1
    elif i=="o":
        s+=1
if 2*c==s:
    print("Yes")
else:
    print("No")
    
    