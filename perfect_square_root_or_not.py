n=int(input())
c=0
for i in range(int(n**0.5)+1):
    if i*i==n:
        c=1
if c==1:
    print(True)
else:
    print(False)
        