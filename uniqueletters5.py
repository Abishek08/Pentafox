a=input()
b=input()
ans=''
for i in a:
    if i in b:
        continue
    else:
        ans+=i
for i in b:
    if i in a:
        continue
    else:
        ans+=i
print(ans)