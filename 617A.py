x=int(input())
step=0

while x>0 :
    if x>=5 :
        x-=5
        step+=1
    elif x>=4 :
        x-=4
        step+=1
    elif x>=3 :
        x-=3
        step+=1
    elif x>=2 :
        x-=2
        step+=1
    elif x>=1 :
        x-=1
        step+=1
print(step)
