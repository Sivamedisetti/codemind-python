a,b,c=map(int,input().split())
import math
s=(a+b+c)/2
d=s*(s-a)*(s-b)*(s-c)
m=math.sqrt(d)
print(format(m,".2f"))
