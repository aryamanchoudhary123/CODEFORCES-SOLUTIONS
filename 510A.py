n,m=map(int,input().split())
c=0
for i in range(n):
    for j in range(m):
        
        if i%2==0 :
            print("#",end="")
            pass
        elif i%2!=0 and c%2==0:
            if j==m-1 :
               print("#",end="")
               pass     
            else :
                print(".",end="")
                pass
                
        elif i%2!=0 and c%2!=0  :
            if j==0 :
               print("#",end="")
               pass
            else :
                print(".",end="")
                pass
    print("")
    if i%2!=0 :c+=1
    
