#318A
'''
#basic approach
n=[]
n = input().split(' ')
a=[]
b=[]
for i in range(1, int(n[0])+1 ):
    if(i%2!=0):
        a.append(i)
    else:
        b.append(i)

z = a+b
# print(z)
print(z[int(n[1])-1])
'''

#diff
n=[]
n = input().split(' ')
a=[]
b=[]
for i in range(1, int(n[0])+1 ):
    if(i%2!=0):
        a.append(i)
    else:
        b.append(i)

aset = set(a)
bset = set(b)

print(aset)