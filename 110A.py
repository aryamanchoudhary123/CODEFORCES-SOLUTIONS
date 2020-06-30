n=int(input())
c=0

while n>0 :
    if n%10 ==4 or n%10==7 :
        c+=1
    n=n//10
if c==0:
    ch='n'
else :    
    ch='p'
while ch=='p' and c>0 :
    if c%10 != 4 and c%10 !=7 :
        ch='n'
        break
    c=c//10


print("YES") if ch=='p' else print("NO")
    
    
