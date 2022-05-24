x = int(input())
y = int(input())
l = 0
for i in range(x,y+1):
    b = len(str(i))
    c=i
    while c!=0:
        v = c%10
        if v!=0 and i%v==0:
            l+=1
        c = c//10
    if l==b:
        print(i,end=" ")
    l=0