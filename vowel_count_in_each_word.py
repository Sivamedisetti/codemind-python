def vowel(n):
    c=0
    for i in n:
        if i in "aeiou":
            c+=1
    return c
l=list(map(str,input().split()))
k=[]
for i in l:
    k.append(vowel(i))
print(*k)