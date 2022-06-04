def vowel(n):
    c=0
    for i in n:
        if i in "aeiou":
            c+=1
    return c
l=list(map(str,input().split()))
s=[]
for i in l:
    s.append(vowel(i))
print(s.count(min(s)))
    
    