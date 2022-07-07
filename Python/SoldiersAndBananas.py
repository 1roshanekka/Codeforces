n = input()
l = []
l = n.split(' ')

PriceOfBanana = int(l[0])
Balance = int(l[1])
NoOfBananas = int(l[2])

TotalPrice = 0
for i in range(1,NoOfBananas+1):
    k = i*PriceOfBanana
    TotalPrice = TotalPrice + k

Borrow = TotalPrice-Balance
if(Borrow>0):
    print(Borrow)
else:
    print(0)

