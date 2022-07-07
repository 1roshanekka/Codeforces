#734A

n = int(input())
x = input()

z = []
for each in x:
    z.append(each)

s = set(z)

d = {}

# for each in s:
#     d[each] = 0

#direct entry of default dictionary
d['A']=0
d['D']=0

for each in z:
    d[each] = d[each] + 1

# print(d)

if(d['D']==0 or d['A']==0):
    if('D' in x):
        print('Danik')
    else:
        print('Anton')
else:        
    if(d['A']>d['D']):
        print('Anton')
    elif(d['A']<d['D']):
        print('Danik')
    else:
        print('Friendship')


# flag = 0
# count = 0

# for i in range(len(x)-1):
#     if((x[i]!=x[i+1])):
#         count = count +1

# print(count,'count')
# if(count == (len(x)-1)):
#     flag = 1

# print(flag,'flag')

# if(flag==1):
#     print('entered')
#     if( (d['A']==d['D']) ):
#         print('Friendship') 
# else:
#     print('out')
#     if(d['A']>d['D']):
#         print('Anton')
#     elif(d['A']<d['D']):
#         print('Danik')
#     else:
#         print('Friendship')
