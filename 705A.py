n=int(input())

arr=[' that ',' it']
mood=[' love',' hate']
i=1
ans=""
while i<=n :
    if i%2!=0 :
        ans+="I" + mood[1] 
    elif i%2==0 :
        ans+="I" + mood[0]

    if i!=n :
        ans+=arr[0]
    elif i==n :
        ans+=arr[1]
    i+=1    

print(ans)        
