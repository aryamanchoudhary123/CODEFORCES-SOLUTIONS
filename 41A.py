s=input()
t=input()
n=len(s)
m=len(t)




if m==n :
    ch='p'
    for i in range(n):
        if s[i] != t[n-1-i] :
            ch='n'
            break

    print("YES") if ch=='p' else print("NO")    

else :
    print("NO")
