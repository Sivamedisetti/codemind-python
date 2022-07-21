s=list(map(str,input().split()))
s=s[len(s)-1]
n=min(s)
if n>='A' and n<='Z':
    if n.lower() in s:
        print(n.lower())
    else:
        print(n)
else:
    print(n)