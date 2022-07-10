n=input()
s=0
for i in range(len(n)):
    s+=int(n[i])**(i+1)
if int(n)==s:
    print(True)
else:
    print(False)
    
