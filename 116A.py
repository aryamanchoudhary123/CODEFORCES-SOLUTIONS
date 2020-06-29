n=int(input())
p=[]
passengers=0
for i in range(n):
    a,b=map(int,input().split())
    passengers=passengers-a+b

    p.append(passengers)

print(max(p))
