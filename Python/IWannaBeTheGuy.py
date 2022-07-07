# #469A
# n = int(input())
# a = []
# a = input().split(' ')
# b = []
# b = input().split(' ')

# count = 0
# for i in range(1,n+1):
#     x = False
#     y = False
#     x = (str(i) in a)
#     y = (str(i) in b)
#     if(x or y):
#         count = count +1

# print(a)
# print(b)
# if(count == n ):
#     print('I become the guy.')
# else:
#     print('Oh, my keyboard!')

n = int(input())
a = []
a = input().split(' ')
a.remove(a[0])
b = []
b = input().split(' ')
b.remove(b[0])

# print(a,b)
x = a + b

ze = set(x)
# print(ze)
# print(len(ze))

count = 0
for i in range(1, n+1):
    if(str(i) in ze):
        count = count +1

if(count==n):
    print('I become the guy.')
else:
    print('Oh, my keyboard!')