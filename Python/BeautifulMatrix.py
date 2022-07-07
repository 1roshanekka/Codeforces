#263A
# i row
# j column
row = []
for i in range(5):
    x = input()
    l = []
    l = x.split()
    row.append(l)
# print(row)

rowposition = 0
columnposition = 0

for i in range(5):
    for j in range(5):
        if(row[i][j]!='0'):
            columnposition = j+1
            rowposition = i+1

moves = 0
# print(rowposition, 'rowposition')
# print(columnposition, 'columnposition')
x = abs(3-int(rowposition))
y = abs(3-int(columnposition))
print(x+y)