n=input()
l=list(n)
b=set(n)
if len(l)==len(b):
    print("Unique Number")
else:
    print("Not Unique Number")