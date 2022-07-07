#344A
n = int(input())
count = 0
for i in range(n):
    x = input()
    if(i>0):
        if(x!=z):
            count = count + 1
    z = x
#count represents no of changes but last one is the extra magnet which is not counted so i have added +1
print(count+1) 