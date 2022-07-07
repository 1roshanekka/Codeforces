#467A
n = int(input())

count = 0
for i in range(n):
    k = input()
    l = []
    l = k.split(' ')
    #p is number of people that already live in the ith room
    #q is capacity of the room
    p = int(l[0])
    q = int(l[1])
    
    if((q-p)>1):
        count = count +1

print(count)