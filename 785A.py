c=0
for _ in range(int(input())):
    s=input()
    s=s.lower()
    if s=="cube":
        c+=6
    elif s=="tetrahedron":
        c+=4
    elif s=="octahedron":
        c+=8
    elif s=="dodecahedron":
        c+=12
    elif s=="icosahedron":
        c+=20

print(c)        
        
               
