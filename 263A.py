arr=[[0 for i in range(5)] for j in range(5)]
x=0
y=0
for i in range(5):
    l=list(map(int,input().split()))
    for j in range(5):
        arr[i][j]=l[j]
        if arr[i][j]==1 :
            x=i
            y=j
            break
        

c=0
c=c+abs(x-2)
c=c+abs(y-2)
print(c)
