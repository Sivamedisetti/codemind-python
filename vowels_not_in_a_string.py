n=input()
s='aeiou'
k=[]
c=0
for i in n:
    if i in s:
        k.append(i)
for j in s:
    if j  in k:
        pass
    else:
        print(j,end=' ')
        c=1
if c==0:
    print("0")