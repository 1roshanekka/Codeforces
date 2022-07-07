#112A
a = input()
b = input()

aFix = a.lower()
bFix = b.lower()

case1 = (aFix>bFix)
case2 = (bFix>aFix)
case3 = (aFix==bFix)

if(case3):
    print(0)
elif(case1):
    print(1)
elif(case2):
    print(-1)