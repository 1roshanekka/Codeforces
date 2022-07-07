#141A
a = input()
b = input()
c = input()

#removing method

l = []
#list of all leters in c

for i in range(len(c)):
    l.append(c[i])

print(len(l))

count = 0
flag = 0
for each in a:
    if(not each in l):
        flag = 1
    else:
        l.remove(each)
        count = count + 1

print(len(l), ' is len of l')
print('len a, count, len(l)')
print(len(a),count,len(l))

record = 0
for every in b:
    if(not every in l):
        flag = 1
    else:
        l.remove(every)
        record = record + 1

print('len b, record, len(l)')
print(len(b),record,len(l))

print('prev')
if(len(l)==0):
    print('YES')
else:
    print('NO')

print('final')
if(flag==1):
    print('NO')
else:
    print('YES')