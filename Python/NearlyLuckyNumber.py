#110A
n = input()
count=0
for each in n:
    # print(each)
    if(each=='4' or each=='7'):
        count = count + 1
# print(count, ' count')
# print(len(n),'len n')
if(count==4 or count==7):
    print('YES')
else:
    print('NO')
