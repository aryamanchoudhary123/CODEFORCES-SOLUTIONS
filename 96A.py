s=input()
n=len(s)
c=1
ans="NO"
for i in range(1,n):
   if s[i]==s[i-1]:
       c+=1
       if c==7 :
           ans="YES"
           break
   else :
       c=1

print(ans)       
       
    
