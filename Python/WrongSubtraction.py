#977A
n = input()
l = []
l = n.split(' ')
num = int(l[0])
k = int(l[1])

#verified
'''
print(num, type(num))
print(k, type(k))
'''

#count no of digits
count = 0
getDig = num
if(getDig==0):
    x = count
else:
    while(getDig>0):
        getDig = getDig//10
        count = count + 1
    x = count
# print(x, type(x), 'digits')

# x is the number of digits 
# k times subtract 1

for i in range(k):
    #get last digit
    dig = 10**(x-1)
    algo = num%dig
    # print(algo, 'algo')
    if((num%10)!=0):
        num = num - 1
    else:
        num = int(num/10)
    # print(num,'this')
    #count no of digits
    count = 0
    getDig = num
    if(getDig==0):
        x = count
    else:
        while(getDig>0):
            getDig = getDig//10
            count = count + 1
        x = count

print(num)




