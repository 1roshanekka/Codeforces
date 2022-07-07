#266A
n = int(input())
if(1<=n<=50):
    s = input()
    l=[]
    count = 0
    #input for list
    for i in range(len(s)):
        l.append(s[i])
    # print(l)

    for i in range(len(l)-1):
        if(l[i]==l[i+1]):
            count = count +1
    print(count)