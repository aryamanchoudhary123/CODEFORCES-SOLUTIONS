n=int(input())
arr=list(map(int,input().split()))
c=0
for i in range(1,n):
    j=arr[0:i]
    if arr[i] > max(j) or arr[i]<min(j):
        c+=1
print(c)        
