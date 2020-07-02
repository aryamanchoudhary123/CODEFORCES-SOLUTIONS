s=list(input())
s=s[1:-1]
x=[]
for i in s :
    if i!=' ' and i!=',' :
        x.append(i)
s=set(x)
print(len(s))
