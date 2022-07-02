n=input()
s,p=0,1
for i  in n:
    i=int(i)
    s+=i
    p*=i
#print(s,p)
if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")
    
