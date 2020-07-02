n=int(input())
s=input()
s=s.lower()

if n<26 :
    ans="NO"
else :
    s=set(s)
    if len(s)==26 :
        ans="YES"
    else :
        ans="NO"

print(ans)        
