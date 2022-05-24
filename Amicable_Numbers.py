x=int(input())
y=int(input())
s,a=0,0
for i in range(1,x):
    if x%i==0:
        s+=i
for j in range(1,y):
    if y%j==0:
        a+=j
if s==y and a==x:
    print("Amicable")
else:
    print("Not Amicable")
    