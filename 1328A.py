for _ in range(int(input())):
    a,b=map(int,input().split())
    if a>b and a%b!=0: 
        print(b-(a%b))
    elif a%b==0 :
        print(0)
    else :
        print(b-a)
