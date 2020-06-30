n=int(input())

arr=[]
c=1
for _ in range(n):
    arr.append(int(input()))

for i in range(n-1) :
    if arr[i] != arr[i+1] :
        c+=1

print(c)        
