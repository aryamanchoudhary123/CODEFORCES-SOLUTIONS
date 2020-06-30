n,t=map(int,input().split())
s=list(input())
c=0
while t>0 :
    t-=1
    i=0
    while i < n-1:
        if s[i]=="B" and s[i+1]=="G":
            s[i]="G"
            s[i+1]="B"
            i+=1
        i+=1    
        
print(''.join(s))
