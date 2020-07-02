for _ in range(int(input())):
    n=list(input())
    arr=[]
    n.reverse()

    for i in range(len(n)) :
        x=int(n[i])%10
        if x!=0 :
            x=x*(10**i)
            arr.append(x)

    arr.reverse()
    print(len(arr))
    for i in arr :
        print(i,end=" ")

