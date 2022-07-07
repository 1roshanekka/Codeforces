n = int(input())
z = []
x = input()
z = x.split()

#Gravity pulls towards the right 

# print(n)
# print(z)

c = []
for i in range(n):
    a = []
    for j in range(int(z[i])):
        a.append('1')
    c.append(a)

print(c)

for i in range(n):
    for j in range()