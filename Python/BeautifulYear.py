#271A
n = input()
if 1000<=int(n)<=9000:
    x = int(n)
    while x>1:
        x = x+1
        y = str(x)
        l = []
        for each in y:
            l.append(each)
        st = set(l)
        # print(l,'list')
        # print(st,'set')
        if(len(st)==len(l)):
            break

print(x)