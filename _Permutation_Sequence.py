from itertools import *
a,b = map(int,input().split())
m = permutations(range(1,a+1))
m = list(m)
for i in m[b-1]:
    print(i,end="")