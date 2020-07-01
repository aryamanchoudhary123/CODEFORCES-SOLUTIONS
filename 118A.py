s=input()
s=s.lower()
ans=""
i=0
while i <len(s):
    if s[i]=="a" or s[i]=="e" or s[i]=="y" or s[i]=="o" or s[i]=="u" or s[i]=="i" :
        i+=1
    else:
        ans+="."+s[i]
        i+=1
print(ans)        
