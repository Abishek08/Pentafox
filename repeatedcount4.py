n=input()
lst=list(n.split())
ans=[]
for i in lst:
    t=''
    for j in i:
        for x in j:
            if x not in t:
                t+=x 
                if i.count(x)==1:
                    continue
                else:
                    t+=str(i.count(x))
    ans.append(t)
print(*ans)