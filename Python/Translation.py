#41A
s = input()
t = input()

k=''
for i in range(len(s)-1,-1,-1):
    k = k + s[i]
if(t==k):
    print('YES')
else:
    print('NO')