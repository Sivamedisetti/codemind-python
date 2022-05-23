x,y = map(int,input().split())
l=len(str(x))
v=x%(10**y)
while x!=0:
    m=x%10**(l-y)
    x=x//10**(l-y)
print(abs(v-m))