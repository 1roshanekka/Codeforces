#282A
n = int(input())

x = 0
for i in range(n):
    l = []
    k = input()
    for each in k:
        if(each=='+'):
            x = x+1
            break
    for each in k:
        if(each == '-'):
            x = x-1
            break
    
print(x)