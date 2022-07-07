#486A

#aam zindagi
'''
n = int(input())
indiv = []
for i in range(n+1):
    e = (-1)**i
    indiv.append(e)

num = []
for j in range(n+1):
    num.append(j)

pro = []
for k in range(n+1):
    x = indiv[k]*num[k]
    pro.append(x)

sum = float(0)
for z in range(n+1):
    sum = sum + pro[z]
    
print()
print(indiv)
print(num)
print(pro)
print(int(sum))
'''

#mentos zindagi
n = int(input())
if(n==0):
    print(0)
else:
    if(n%2==0):
        print(n//2)
    else:
        print(-n//2)