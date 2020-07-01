n=int(input())
x=list(map(int,input().split()))
p=x[0]
x=x[1:]
y=list(map(int,input().split()))
q=y[0]
y=y[1:]
ans="I become the guy."
for i in range(1,n+1):
    if i not in x and i not in y : ans="Oh, my keyboard!"

print(ans)    
