#96A
n = input()
count = 0
for i in range(len(n)-1):
    if(n[i]==n[i+1]):
        count = count +1
    elif(count>=6):
        break
    else:
        count = 0

if(count>=6):
    print('YES')
else:
    print('NO')

