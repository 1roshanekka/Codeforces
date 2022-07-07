#520A
l=[]
m = input()
s = input()
n = s.lower()
for x in n:
    if x.isalpha():
        l.append(x)

a = set(l)

# print(a)

if(len(a)==26):
    print('YES')
else: 
    print('NO')