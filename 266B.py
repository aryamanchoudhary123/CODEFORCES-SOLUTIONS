n,t=map(int,input().split())
s=list(input())
c=0
for i in range(n-1):
    if s[i]=="B":
        for j in range(i+1,n-1):
            if c < t:
                if s[j]=="G" :
                    s[i],s[j]=s[j],s[i]
                    c+=1 

print(''.join(s))
