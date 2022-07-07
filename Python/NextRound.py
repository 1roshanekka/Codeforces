#158A
n = input()
l=[]
l = n.split(' ')
a = input()
l1=[]
l1 = a.split(' ')
s=[]
for i in range(len(l1)):
    s.append(int(l1[i]))
s.sort(reverse=True)
# if
# x = s[int(l[1])]

count = 0
for j in range(len(s)):
    if(s[j]>0):
        x = s[int(l[1])-1]
        if(s[j]>=x):
            count = count + 1

print(count)
















# #158A
# n = input()
# l = []
# l = n.split(' ')
# # print(l)
# a = input()
# l2 = []
# l2 = a.split(' ')
# # print(l2)
# count =0
# for j in range(len(l2)):
#     if(int(l2[j]))>=int(l[1]):
#         count = count +1
#         # print(count, 'this')

# print(count)