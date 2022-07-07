#58A
#n is the variable which stores the input
n = input()
d = {}
#this code counts the number of occurences of each letter
#donot change sequence of code
'''
h = n.count('h')
e = n.count('e')
l = n.count('l')
o = n.count('o')
print('h', h)
print('e', e)
print('l', l)
print('o', o)
'''

d = {}
#initiate 
s = set(n)
for each in s:
    d[each] = 0

print(d) #initialized dictionary

#alloting dictionary
for each in n:
    d[each] += 1

print(d) #computed dictionary

#putting in list
x = []
for i in range(len(n)):
    x.append(n[i])
print()
print('initial list')
print(x)

'''
for i in range(len(x)):
    if(x[i]!='h'):
        x.remove(x[i])
    else:
        break
'''  


for each in x:
    # print()
    # print(f'printing each variable - {each}')
    # print(each=='h' or each=='e' or each=='l' or each=='o')
    if(each=='h' or each=='e' or each=='l' or each=='o'):
        continue
    else:
        # print(f'--> removing {each}')
        x.remove(each)


#removed list x

print()
print('removed list x')
print(x)

#removing duplicates
#using index

#remove h duplicates
h1 = x.count('h')
while(h1>1):
    x.remove('h')
    h1 = x.count('h')

e1 = x.count('e')
while(e1>1):
    x.remove('e')
    e1 = x.count('e')

l1 = x.count('l')
while(l1>2):
    x.remove('l')
    l1 = x.count('l')

o1 = x.count('o')
while(o1>1):
    x.remove('o')
    o1 = x.count('o')

print(x)

#putting in string
st = ''
for i in range(len(x)):
    st += x[i]
print(st)

if('hello' in st):
    print('YES')
else:
    print('NO')

#removes h first instead of removing h which is in middle
