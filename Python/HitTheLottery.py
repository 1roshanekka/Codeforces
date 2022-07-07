#996A
n = int(input())

#denominations are 1,5,10,20,100
#withdraw minimum no of cash

nos = 0
ls = []

def cls():
    global ls
    ls = []
    return

def count(x) :
    if(x//100>0):
        ls.append(x//100)
        ls.append(100*(x//100))
        return int(ls[0])
    elif(x//20>0):
        ls.append(x//20)
        ls.append(20*(x//20))
        return int(ls[0])
    elif(x//10>0):
        ls.append(x//10)
        ls.append(10*(x//10))
        return int(ls[0])
    elif(x//5>0):
        ls.append(x//5)
        ls.append(5*(x//5))
        return int(ls[0])
    elif(x//1>0):
        ls.append(x//1)
        ls.append(1*(x//1))
        return int(ls[0])

while(n>0):
    nos += count(n)
    n -= int(ls[1])
    # print(ls)
    cls()

print(nos)

    