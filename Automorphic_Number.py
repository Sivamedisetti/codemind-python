x = int(input())
b = x**2
c = len(str(x))
d = b%(10**c)
if d==x:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')