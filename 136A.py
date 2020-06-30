n=int(input())
arr=list(map(int,input().split()))
ans=[0 for i in range(n)]

for i in range(n):
    ans[arr[i]-1]=i+1

for i in ans :
    print(i,end=" ")
