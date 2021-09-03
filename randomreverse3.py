import random
letters="Pentafox"
l=letters[::-1]
a=l.lower()
m=random.sample(letters,1)
d=''.join(map(str,m))
b=d.upper()
c=b+a
print(c)