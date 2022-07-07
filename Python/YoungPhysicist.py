#69A
from re import L


n = int(input())
l= []
for i in range(n):
    m = input()
    a = m.split()
    l.append(a)

'''
Vector 
Equillibrium if sum of vectors is 0
Therefore   A = Ax + Ay + Az
            B = Bx + by + Bz
Sum of Vector in x is Ax + By should be 0 for being in equllibrium
'''
x = 0
y = 0
z = 0
for i in range(n):
    x = x + int(l[i][0])
    y = y + int(l[i][1])
    z = z + int(l[i][2])

if(x==0 and y==0 and z==0):
    print('YES')
else:
    print('NO')

# print(l)
