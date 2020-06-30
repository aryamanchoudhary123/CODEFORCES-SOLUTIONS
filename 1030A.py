n=int(input())
arr=list(map(int,input().split()))
ans="EASY"
for i in arr:
    if i==1 :
        ans="HARD"
        break
print(ans)    
