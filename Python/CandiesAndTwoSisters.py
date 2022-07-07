import math
l =[]

n = int(input())
if(1 <= n <= math.pow(10,4)):
    while(n>0):
        a = int(input())
        if( 1 <= a <= (2*math.pow(10,9))):
            l.append(a)
            n = n-1
            # print()
            # print(n,'round')
            # print()
            # working!!
# print(l) 
#Working!!

print()

lis =[]
for i in range(len(l)):
    x = l[i] 
    count = 0

    w=x-1
    if(x==2 or x==1):
        lis.append(0)
    else:
        lis.append(w//2)
    # elif(w%2==0):
    #     lis.append(w//2)
    # elif(w%2!=0):
    #     lis.append((w//2))
    
        

    # w = x//2
    # if(x==2 or x ==1):
    #     lis.append(0)
    # elif(w%2==0):
    #     lis.append(int(w)-1)
    # else:
    #     lis.append(int(w))
    #Classic method but takes more time(INEFFICIENT)

    '''
    for j in range(x-1,x//2,-1):
        for k in range(1,(x//2)+1):
            if((j+k)==x):
                # print(j,k,x)
                count = count +1
    # print(count)
    lis.append(count)
    '''

    '''
    # if(x>=2):
    #     a = math.factorial(x)
    #     # print(a)
    #     b = math.factorial(x-2)
    #     permut = a//b
    #     # print(permut)
    #     secret = x*2
    #     # print(secret)
        
    #     fin = permut//secret
    #     lis.append(fin)

    # else:  
    #     for j in range(x-1,x//2,-1):
    #         for k in range(1,(x//2)+1):
    #             if((j+k)==x):
    #                 # print(j,k,x)
    #                 count = count +1
    #     # print(count)
    #     lis.append(count)
    '''


for i in range(len(lis)):
    print(lis[i])







# n = float(input())
# if(1 <= n <= math.pow(10,4) ):
#     #if number other than below criteria not fulfilled then input again
#     while(n>0):
#         a = float(input())
#         if(1 <= a <= (2*math.pow(10,9)) ):
#             l.append(a)
#             n = n -1