x='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n=input()
lst=list(n.split(','))
print(lst)
for i in lst:
    t=int(i)-1
    print(x[t],end="")