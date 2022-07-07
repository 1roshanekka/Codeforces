#133A
n = input()
count = 0
l=[]

d={}
#initializaion
d['H']=[]
d['Q']=[]
d['9']=[]
d['+']=[]

#stores location
for i in range(len(n)):
    if(n[i]=='H'):
        d['H'].append(i+1)
        count = count +1
    elif(n[i]=='Q'):
        d['Q'].append(i+1)
        count = count +1
    elif(n[i]=='9'):
        d['9'].append(i+1)
        count = count +1
    elif(n[i]=='+'):
        d['+'].append(i+1)
        count = count +1


#check if + is in between two operation
z = []
z = ['H','Q','9']

'''
i in not used
for i in range(len(n)):
    if(n[i]=='+'):
    if( ('H' in n)and('Q' in n) ):
        if(n.index('H')<n.index('+')<n.index('Q')):
            print('Safe')
        elif(n.index('Q')<n.index('+')<n.index('H')):
            print('Safe')

    if( ('H' in n)and('9' in n) ):
        if(n.index('H')<n.index('+')<n.index('9')):
            print('Safe')
        elif(n.index('9')<n.index('+')<n.index('H')):
            print('Safe')

    if( ('Q' in n)and('9' in n) ):
        if(n.index('Q')<n.index('+')<n.index('9')):
            print('Safe')
        elif(n.index('9')<n.index('+')<n.index('Q')):
            print('Safe')

print(n.index('9')<n.index('+')<n.index('H'))
def func():
    check indices of + and find if its in middle
'''

res = ''
for i in range(len(n)):
    if(n[i]=='+'):
        k = n[0:i]
        m = n[i+1:len(n)+1]
        if( ('H' in k)and('Q' in m) ):
            res = ('safe in HQ')
        elif( ('H' in n)and('9' in n) ):
            res = ('safe in H9')
        elif( ('Q' in n)and('9' in n) ):
            res = ('safe in Q9')
'''
# def safe():
#     o = ''
#     if(n[i]=='+'):
#         k = n[0:i]
#         m = n[i+1:len(n)+1]
#         if( ('H' in k)and('Q' in m) ):
#             print('safe in HQ')
#             o = 'a'
#         elif( ('H' in n)and('9' in n) ):
#             print('safe in H9')
#             o = 'b'
#         elif( ('Q' in n)and('9' in n) ):
#             print('safe in Q9')
#             o = 'c'
#         if(o=='a' or o=='b' or o=='c'):
#             return True
#         else:
#             return False
# print(safe())
'''

def plus():
    if('+' in n):
        return True
    else:
        return False

# print(func())

if(count!=0):
    if(plus() and (res == ('safe in HQ') or res == ('safe in H9') or res == ('safe in Q9'))):
        print('YES')
    elif(not plus()):
        print('YES')
    else:
        print('NO')
    # if(func()):
    #     print('YES')
    # else:
    #     print('NO')
else:
    print('NO')

print(d)


'''

#133A
n = input()
count = 0

def check(x):
    if(x=='H'):
        return True
    elif(x=='Q'):
        return True
    elif(x=='9'):
        return True
    elif(x=='+'):
        return True


for each in n:
    if(check(each)):
        count = count +1
        
# print(count)

def func():
    if(count%2==0):
        return False
    elif(count>=3):
        return True
    else: 
        return False

# print(func())

if(count!=0):
    if(func()):
        print('YES')
    else:
        print('NO')
else:
    print('NO')

'''
