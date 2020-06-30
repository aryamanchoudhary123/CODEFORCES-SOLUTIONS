n=int(input())
n+=1
while True:
    temp=n
    t=[]
    ch='p'
    while(temp>0) :
        x=temp%10
        if x not in t:
            t.append(x)
        elif x in t :
            ch='n'
            break
        temp=temp//10
    if ch=='p' :
        print(n)
        break
    else :
        n+=1 
        
