
n = int(input())
term = []
term1 = []
x = input()
term = x.split()
for i in range(n):
    q = int(term[i])
    term1.append(q)

print(term1)
d = []
for i in range(n-1):
    d.append(term1[i+1]//term1[0])
print(d)
