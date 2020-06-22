n=int(input())
c=0
for _ in range(n):
    arr=list(map(int,input().split()))

    if arr.count(1)>=2 :
        c+=1
print(c)
