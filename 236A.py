s=list(input())
char=[]

for i in s:
    if i not in char :
        char.append(i)

if len(char)%2==0 :
    print("CHAT WITH HER!")

else:
    print("IGNORE HIM!")
    
