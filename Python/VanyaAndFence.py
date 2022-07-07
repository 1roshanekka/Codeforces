#677A
n, h = map(int, input().split())
x = input()
l = []
l = x.split(' ')

#number of people who is going to bend
count = 0
for each in l:
    if(int(each)>h):
        count = count +1

print((count*2)+(n-count))
# n, h = map(int, input().split())
# print(n,h)