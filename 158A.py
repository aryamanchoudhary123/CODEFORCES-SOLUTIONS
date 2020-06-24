n,k=map(int,input().split())
arr=list(map(int,input().split()))
c=0
for i in arr :
    if i >=arr[k-1] and i!=0:
        c+=1
print(c)

