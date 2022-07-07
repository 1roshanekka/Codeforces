#133A
n = input()
count = 0
l=[]

if( ('H' in n) or ('Q' in n) or ('9' in n) ):
    print('YES')
elif( ( ('H' in n) or ('Q' in n) or ('9' in n) ) and '+' in n):
    print('YES')
else:
    print('NO')