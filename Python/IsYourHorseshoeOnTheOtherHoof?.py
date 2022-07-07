#228A
n = input()
l=[]
l = n.split(' ')
# print(l)

count = 0

a = l[0] ; b = l[1] ; c = l[2] ; d = l[3]

#dictionary approach
d={}
a = set(l)
for each in a:
    d[each] = 0

# print(d)

for each in l:
    if(each in d):
        d[each] = d[each]+1

# print(d)
x=[]
for each in d:
    x.append(d[each])
# print(x)

if(len(x)==1):
    print(3)
elif(len(x)==2):
    # if(x[0]==2 and x[1]==2):
    #     print(2)
    # else:
    #     print()
    print(2)
elif(len(x)==3):
    print(1)

elif(len(x)==4):
    print(0)


#______________________________________________program ends here

# empty=0
# while(len(l)>0):
#     x=0
#     a = l[0]
#     for i in range(len(l)):
#         if(l[i]==a):
#             x = x+1
#     if(x>=2):
#         break
#     else:
#         l.remove(a)
#         empty = empty +1

# if(empty==4):
#     print(0)

# for i in range(len(l)):
#     if(l[i]==a):
#         count = count +1



# if(count==1):
#     print(0)
# elif(count==2):
#     print(1)
# elif(count==3):
#     print(2)
# elif(count==4):
#     print(3)
