s=input()
l=0
u=0

for i in (s):
    if i.islower() :
        l+=1
    elif i.isupper() :
        u+=1

if u<=l :
    s=s.lower()
else :
    s=s.upper()

print(s)    
