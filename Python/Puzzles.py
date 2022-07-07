
n,m = map(int, input().split())

puzz = []
puzzInt = []

puzz = input().split()
#print(puzz)
#print(len(puzz))


for i in range(len(puzz)):
    puzzInt.append(int(puzz[i]))
#print(puzzInt)
#print(len(puzzInt))

#puzzInt = puzzInt.sort()
lowest = 99999999999
s = set(puzzInt)
sList = list(s)
print(sList)

for i in range(len(sList)):
    for j in range(len(sList)):
        if(sList[i]!=sList[j]):
            if(abs(sList[i]-sList[j])<lowest):
                lowest = abs(sList[i]-sList[j])

print(lowest)
