a,b=map(int,input().split())
x=max(a,b)
y=min(a,b)
print(y,end=" ")

x-=y
print(int(x/2))
