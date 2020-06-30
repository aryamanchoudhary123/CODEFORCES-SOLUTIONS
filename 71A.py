n=int(input())
 
for _ in range(n):
    s=input()
    ans=s
    if len(s)>10 :
        ans=s[0]+str(len(s)-2)+s[-1]
 
    print(ans)    
