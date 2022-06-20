n=list(map(str,input().split()))
count=0
for i in n:
    if(i[0]in'aeiouAEIOU'and i[len(i)-1] not in'aeiouAEIOU'):
        count+=1
print(count)