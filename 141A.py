a=input()
b=input()
ans=list(input())
x="YES"
for i in a :
    if i in ans :
        ans.remove(i)
        
    else :
        x="NO"
        break
if x!="NO":
    for i in b :
        if i in ans :
            ans.remove(i)
           
        else   :
            x="NO"
            break
if len(ans)!=0 :
    x="NO"

print(x)    
                
