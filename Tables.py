x,y=map(int,input().split())
for i in range(1,y+1):
    if i%2!=0:
        print(x,'x',i,'=',x*i)