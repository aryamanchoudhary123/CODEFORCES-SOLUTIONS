n=int(input())
arr=list(map(int,input().split()))

s=0
l=0
t=0

m=max(arr)
for j in range(n):
    if arr[j]==m :
        l=j
        break
t+=l
m=min(arr)
for i in range(n):
    if arr[i]==m :
        s=i
t+=n-1-s

if l>s :
    t-=1

print(t)
    
