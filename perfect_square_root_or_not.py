n=int(input())
for i in range(n//2):
    if i**2==n:
        print(True)
        break
else:
    print(False)
    