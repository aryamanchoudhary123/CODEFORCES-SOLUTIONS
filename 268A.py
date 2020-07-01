h=[]
g=[]
n=int(input())
for _ in range(n):
    x,y=map(int,input().split())
    h.append(x)
    g.append(y)
c=0
for i in range(n):
    for j in range(n):
        if h[i]==g[j] :
            c+=1
print(c)    
