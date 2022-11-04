#785A
n = int(input())
l = []
for i in range(n):
    l.append(input())

# print(l)

def poly(x):
    if(x=='Tetrahedron'):
        return 4
    elif(x=='Cube'):
        return 6
    elif(x=='Octahedron'):
        return 8
    elif(x=='Dodecahedron'):
        return 13
    elif(x=='Icosahedron'):
        return 20

sum = 0
for each in l:
    sum = sum + poly(each)

print(sum)