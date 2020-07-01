n,k=map(int,input().split())

c=240
p=0

c=c-k
for i in range(1,n+1):
    c-=5*i
    if c<0 :
        break
    else :
        p+=1
print(p)    
